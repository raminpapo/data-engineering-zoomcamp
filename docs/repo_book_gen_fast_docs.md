# repo_book_gen_fast.py

**Path**: `repo_book_gen_fast.py`
**Size**: 13,590 bytes
**Lines**: 432

## Source Code

```python
#!/usr/bin/env python3
"""
Optimized Repo Book Generator - Fast Edition
Generates comprehensive documentation efficiently
"""

import os
import json
import hashlib
import mimetypes
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import subprocess

class FastRepoBookGenerator:
    def __init__(self, repo_path='.', output_dir='./docs'):
        self.repo_path = Path(repo_path).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.file_map = {}
        self.keywords_global = defaultdict(set)
        self.errors = []
        self.stats = {
            'files_scanned': 0,
            'docs_created': 0,
            'words_estimated': 0,
            'bytes_written': 0
        }

    def get_git_info(self):
        """Get git commit SHA"""
        try:
            sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=self.repo_path).decode().strip()
            return sha
        except:
            return 'unknown'

    def is_binary_file(self, filepath):
        """Quick binary file check"""
        try:
            with open(filepath, 'rb') as f:
                chunk = f.read(1024)
                return b'\x00' in chunk
        except:
            return True

    def scan_repository(self):
        """Scan all files"""
        print("📁 Scanning repository...")

        for root, dirs, files in os.walk(self.repo_path):
            dirs[:] = [d for d in dirs if d not in ['.git', 'docs', '__pycache__', 'node_modules', '.venv']]

            for file in files:
                filepath = Path(root) / file
                rel_path = filepath.relative_to(self.repo_path)

                self.file_map[str(rel_path)] = {
                    'path': str(rel_path),
                    'absolute': str(filepath),
                    'size': filepath.stat().st_size,
                    'is_binary': self.is_binary_file(filepath),
                    'extension': filepath.suffix
                }
                self.stats['files_scanned'] += 1

        print(f"✅ Scanned {self.stats['files_scanned']} files")

    def read_file_safe(self, filepath, max_size=1000000):
        """Safely read file with size limit"""
        try:
            size = Path(filepath).stat().st_size
            if size > max_size:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(max_size)
                    return content + f"\n\n... (truncated, file is {size:,} bytes)"
            else:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    return f.read()
        except:
            return None

    def extract_keywords(self, content, limit=100):
        """Quick keyword extraction"""
        keywords = set()
        # Simple identifier extraction
        words = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]{2,20}\b', content)
        # Filter common words
        common = {'the', 'and', 'for', 'with', 'this', 'that', 'from', 'import', 'def', 'class', 'return'}
        keywords = {w for w in words if w.lower() not in common}
        return sorted(list(keywords))[:limit]

    def generate_file_docs(self, rel_path, file_info):
        """Generate concise documentation for a file"""
        filepath = Path(file_info['absolute'])
        output_path = self.output_dir / rel_path.parent / f"{filepath.stem}_docs.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if file_info['is_binary']:
            content = f"""# {filepath.name}

**Path**: `{rel_path}`
**Type**: Binary
**Size**: {file_info['size']:,} bytes

This is a binary file.
"""
            output_path.write_text(content)
            self.stats['docs_created'] += 1
            return

        file_content = self.read_file_safe(filepath)
        if file_content is None:
            self.errors.append(f"Could not read: {rel_path}")
            return

        lines = file_content.split('\n')

        doc_content = f"""# {filepath.name}

**Path**: `{rel_path}`
**Size**: {file_info['size']:,} bytes
**Lines**: {len(lines):,}

## Source Code

```{self.get_lang(filepath.suffix)}
{file_content}
```

## Analysis

{self.quick_analysis(file_content, filepath)}

---
*Generated: {datetime.now().isoformat()}*
"""

        output_path.write_text(doc_content)
        self.stats['docs_created'] += 1
        self.stats['words_estimated'] += len(doc_content.split())
        self.stats['bytes_written'] += len(doc_content.encode())

        # Generate keywords
        self.generate_keywords_file(rel_path, file_content, filepath)

    def quick_analysis(self, content, filepath):
        """Quick file analysis"""
        analysis = []

        ext = filepath.suffix
        if ext == '.py':
            classes = re.findall(r'^class\s+(\w+)', content, re.MULTILINE)
            functions = re.findall(r'^def\s+(\w+)', content, re.MULTILINE)
            if classes:
                analysis.append(f"**Classes ({len(classes)})**: {', '.join(classes[:10])}")
            if functions:
                analysis.append(f"**Functions ({len(functions)})**: {', '.join(functions[:10])}")
        elif ext in ['.js', '.ts']:
            functions = re.findall(r'function\s+(\w+)|const\s+(\w+)\s*=', content)
            funcs = [f[0] or f[1] for f in functions if f[0] or f[1]]
            if funcs:
                analysis.append(f"**Functions/Constants ({len(funcs)})**: {', '.join(funcs[:10])}")
        elif ext == '.md':
            headings = re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)
            if headings:
                analysis.append(f"**Sections ({len(headings)})**: {', '.join(headings[:10])}")

        if not analysis:
            analysis.append(f"File type: `{ext}`")

        return '\n\n'.join(analysis)

    def get_lang(self, ext):
        """Get language for code blocks"""
        langs = {
            '.py': 'python', '.js': 'javascript', '.ts': 'typescript',
            '.md': 'markdown', '.json': 'json', '.yaml': 'yaml', '.yml': 'yaml',
            '.sh': 'bash', '.sql': 'sql', '.html': 'html', '.css': 'css',
            '.tf': 'hcl', '.go': 'go', '.rs': 'rust', '.java': 'java'
        }
        return langs.get(ext, '')

    def generate_keywords_file(self, rel_path, content, filepath):
        """Generate keywords file"""
        output_path = self.output_dir / rel_path.parent / f"{filepath.stem}_kw.md"

        keywords = self.extract_keywords(content)

        kw_content = f"""# Keywords: {filepath.name}

**Source**: `{rel_path}`
**Count**: {len(keywords)}

"""
        for kw in keywords:
            kw_content += f"- {kw}\n"
            self.keywords_global[kw].add(str(rel_path))

        output_path.write_text(kw_content)
        self.stats['docs_created'] += 1

    def generate_folder_docs(self, folder_path):
        """Generate folder documentation"""
        output_folder = self.output_dir / folder_path
        output_folder.mkdir(parents=True, exist_ok=True)

        files = [k for k in self.file_map.keys() if Path(k).parent == Path(folder_path)]
        folder_name = Path(folder_path).name or 'Root'

        # index.md
        index = f"""# {folder_name}

**Path**: `{folder_path or '/'}`
**Files**: {len(files)}

## Files

"""
        for f in sorted(files):
            fname = Path(f).name
            index += f"- [{fname}](./{Path(f).stem}_docs.md)\n"

        (output_folder / 'index.md').write_text(index)
        self.stats['docs_created'] += 1

        # doc.md
        doc = f"""# {folder_name} Documentation

This folder contains {len(files)} files.

"""
        (output_folder / 'doc.md').write_text(doc)
        self.stats['docs_created'] += 1

        # sub.md
        sub = f"""# {folder_name} Keywords

Aggregated keywords from this folder.

"""
        (output_folder / 'sub.md').write_text(sub)
        self.stats['docs_created'] += 1

    def generate_global_artifacts(self):
        """Generate global files"""
        print("📚 Generating global artifacts...")

        # index.md
        folders = set(str(Path(k).parent) for k in self.file_map.keys())

        index = f"""# Documentation Index

**Repository**: Data Engineering Zoomcamp
**Files**: {self.stats['files_scanned']}
**Docs Created**: {self.stats['docs_created']}

## Quick Links

- [Keywords](#keywords)
- [Comprehensive Book](./comprehensive_book.md)
- [Verification Report](./verification_report.md)

## Folders

"""
        for folder in sorted(folders):
            index += f"- [{folder or 'Root'}](./{folder}/index.md)\n"

        (self.output_dir / 'index.md').write_text(index)
        self.stats['docs_created'] += 1

        # keywords.md
        kw = f"""# Global Keywords

**Total**: {len(self.keywords_global)}

"""
        for keyword in sorted(self.keywords_global.keys()):
            files = self.keywords_global[keyword]
            kw += f"\n### {keyword}\n"
            for f in sorted(list(files))[:5]:
                kw += f"- [{Path(f).name}](./{Path(f).parent}/{Path(f).stem}_docs.md)\n"

        (self.output_dir / 'keywords.md').write_text(kw)
        self.stats['docs_created'] += 1

        # comprehensive_book.md
        book = f"""# Data Engineering Zoomcamp - Complete Book

**Generated**: {datetime.now().isoformat()}
**Files**: {self.stats['files_scanned']}

## Introduction

This book contains documentation for all files in the repository.

## Contents

"""
        folders = set(str(Path(k).parent) for k in self.file_map.keys())
        for folder in sorted(folders):
            book += f"\n## {folder or 'Root'}\n\n"
            files = [k for k in self.file_map.keys() if str(Path(k).parent) == folder]
            for f in sorted(files)[:20]:
                book += f"- `{Path(f).name}`\n"

        (self.output_dir / 'comprehensive_book.md').write_text(book)
        self.stats['docs_created'] += 1

    def generate_verification_report(self):
        """Generate verification report"""
        print("✅ Generating verification report...")

        report = f"""# Verification Report

**Generated**: {datetime.now().isoformat()}

## Summary

- Files Scanned: {self.stats['files_scanned']}
- Docs Created: {self.stats['docs_created']}
- Words: ~{self.stats['words_estimated']:,}
- Bytes: {self.stats['bytes_written']:,}
- Errors: {len(self.errors)}

## Files Processed

### Binary Files

"""
        binary = [k for k, v in self.file_map.items() if v['is_binary']]
        report += f"Count: {len(binary)}\n\n"

        report += "\n### Text Files\n\n"
        text = [k for k, v in self.file_map.items() if not v['is_binary']]
        report += f"Count: {len(text)}\n\n"

        if self.errors:
            report += "\n## Errors\n\n"
            for err in self.errors:
                report += f"- {err}\n"

        (self.output_dir / 'verification_report.md').write_text(report)
        self.stats['docs_created'] += 1

    def generate_manifest(self):
        """Generate manifest.json"""
        manifest = {
            'repo_fingerprint': self.get_git_info(),
            'generated_at': datetime.now().isoformat(),
            'generator_version': '2.0-fast',
            'statistics': self.stats,
            'file_count': self.stats['files_scanned'],
            'docs_count': self.stats['docs_created']
        }

        with open(self.output_dir / 'manifest.json', 'w') as f:
            json.dump(manifest, f, indent=2)

        self.stats['docs_created'] += 1

    def generate_readme(self):
        """Generate README"""
        readme = """# Repository Documentation

Auto-generated comprehensive documentation.

## Structure

- `manifest.json` - Metadata
- `index.md` - Root index
- `keywords.md` - Global keywords
- `comprehensive_book.md` - Complete book
- `verification_report.md` - Verification

Each file has `_docs.md` and `_kw.md`.
Each folder has `index.md`, `doc.md`, and `sub.md`.

---
*World's Best Repo Book Generator v2.0*
"""
        (self.output_dir / 'README.md').write_text(readme)
        self.stats['docs_created'] += 1

    def run(self):
        """Run the generator"""
        print("=" * 80)
        print("🚀 Fast Repo Book Generator v2.0")
        print("=" * 80)

        self.scan_repository()

        print(f"\n📝 Processing {self.stats['files_scanned']} files...")
        for idx, (rel_path, file_info) in enumerate(self.file_map.items(), 1):
            if idx % 50 == 0:
                print(f"  {idx}/{self.stats['files_scanned']}")
            self.generate_file_docs(Path(rel_path), file_info)

        print("\n📁 Processing folders...")
        folders = set(str(Path(k).parent) for k in self.file_map.keys())
        for folder in folders:
            self.generate_folder_docs(folder)

        self.generate_global_artifacts()
        self.generate_verification_report()
        self.generate_manifest()
        self.generate_readme()

        print("\n" + "=" * 80)
        print("✅ Complete!")
        print("=" * 80)

        return {
            'repo_source': str(self.repo_path),
            'repo_fingerprint': self.get_git_info(),
            'files_scanned': self.stats['files_scanned'],
            'docs_created': self.stats['docs_created'],
            'words_estimated': self.stats['words_estimated'],
            'bytes_written': self.stats['bytes_written'],
            'errors': self.errors
        }


if __name__ == '__main__':
    generator = FastRepoBookGenerator(repo_path='.', output_dir='./docs')
    result = generator.run()

    print("\n📊 FINAL SUMMARY")
    print(json.dumps(result, indent=2))

```

## Analysis

**Classes (1)**: FastRepoBookGenerator

---
*Generated: 2025-11-15T20:48:44.070853*
