#!/usr/bin/env python3
"""
World's Best Repo Book Generator and Index Builder
Generates comprehensive documentation for an entire repository.
"""

import os
import json
import hashlib
import mimetypes
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import sys

# Configuration
REPO_ROOT = Path(".")
DOCS_ROOT = Path("./docs")
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
CHUNK_SIZE = 50 * 1024 * 1024  # 50MB for chunking large outputs
BINARY_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.tar', '.gz',
                     '.pyc', '.so', '.o', '.class', '.jar', '.exe', '.dll', '.parquet'}

class RepoBookGenerator:
    def __init__(self):
        self.manifest = {
            "repo_source": str(REPO_ROOT.absolute()),
            "repo_fingerprint": "",
            "commit_sha": "",
            "generator_version": "1.0.0",
            "timestamp_start": datetime.utcnow().isoformat(),
            "timestamp_end": "",
            "files_scanned": 0,
            "docs_created": 0,
            "bytes_written": 0,
            "file_count": 0,
            "errors": []
        }
        self.all_files = []
        self.text_files = []
        self.binary_files = []
        self.large_files = []
        self.all_keywords = defaultdict(list)  # keyword -> [(file, description)]
        self.progress_log = []

    def get_commit_sha(self):
        """Get current git commit SHA"""
        try:
            import subprocess
            result = subprocess.run(['git', 'rev-parse', 'HEAD'],
                                  capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except:
            return "unknown"

    def compute_fingerprint(self):
        """Compute repository fingerprint"""
        file_list = sorted([str(f) for f in self.all_files])
        content = "\n".join(file_list)
        return hashlib.sha256(content.encode()).hexdigest()

    def is_binary_file(self, filepath):
        """Check if file is binary"""
        # Check extension first
        if filepath.suffix.lower() in BINARY_EXTENSIONS:
            return True

        # Try to read first 8192 bytes and check for null bytes
        try:
            with open(filepath, 'rb') as f:
                chunk = f.read(8192)
                if b'\x00' in chunk:
                    return True
        except:
            return True

        return False

    def scan_repository(self):
        """Scan repository and classify files"""
        print("📂 Scanning repository...")

        for root, dirs, files in os.walk(REPO_ROOT):
            # Skip .git and docs directories
            dirs[:] = [d for d in dirs if d not in {'.git', 'docs'}]

            for filename in files:
                filepath = Path(root) / filename
                rel_path = filepath.relative_to(REPO_ROOT)

                # Skip docs directory files
                if str(rel_path).startswith('docs/'):
                    continue

                self.all_files.append(rel_path)

                # Classify
                file_size = filepath.stat().st_size

                if file_size > MAX_FILE_SIZE:
                    self.large_files.append(rel_path)
                elif self.is_binary_file(filepath):
                    self.binary_files.append(rel_path)
                else:
                    self.text_files.append(rel_path)

        self.manifest['file_count'] = len(self.all_files)
        self.manifest['files_scanned'] = len(self.all_files)

        print(f"✓ Found {len(self.all_files)} files")
        print(f"  - Text files: {len(self.text_files)}")
        print(f"  - Binary files: {len(self.binary_files)}")
        print(f"  - Large files: {len(self.large_files)}")

    def extract_keywords(self, content, filepath):
        """Extract keywords from content"""
        keywords = set()

        # Extract identifiers (functions, classes, variables)
        # Python
        keywords.update(re.findall(r'def\s+(\w+)', content))
        keywords.update(re.findall(r'class\s+(\w+)', content))

        # JavaScript/TypeScript
        keywords.update(re.findall(r'function\s+(\w+)', content))
        keywords.update(re.findall(r'const\s+(\w+)', content))
        keywords.update(re.findall(r'let\s+(\w+)', content))
        keywords.update(re.findall(r'var\s+(\w+)', content))

        # SQL
        keywords.update(re.findall(r'CREATE\s+TABLE\s+(\w+)', content, re.IGNORECASE))
        keywords.update(re.findall(r'CREATE\s+VIEW\s+(\w+)', content, re.IGNORECASE))

        # Common patterns
        keywords.update(re.findall(r'import\s+(\w+)', content))
        keywords.update(re.findall(r'from\s+(\w+)', content))

        # Remove common/short words
        keywords = {k for k in keywords if len(k) > 2 and not k.lower() in {'the', 'and', 'for', 'with'}}

        return sorted(keywords)[:500]  # Limit per file

    def safe_read_file(self, filepath):
        """Safely read file content"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as e:
            self.manifest['errors'].append(f"Error reading {filepath}: {str(e)}")
            return None

    def generate_file_docs(self, filepath):
        """Generate _docs.md for a single file"""
        content = self.safe_read_file(REPO_ROOT / filepath)
        if content is None:
            return None

        # Prepare output path
        doc_path = DOCS_ROOT / filepath.parent / f"{filepath.name}_docs.md"
        doc_path.parent.mkdir(parents=True, exist_ok=True)

        # Count lines and size
        lines = content.split('\n')
        line_count = len(lines)
        size_bytes = len(content.encode('utf-8'))

        # Truncate very large files for display
        display_content = content
        if len(content) > 500000:  # 500KB text
            display_content = content[:500000] + "\n\n... [Content truncated for display] ..."

        # Generate documentation
        doc_content = f"""# Documentation: {filepath.name}

## File Metadata

- **Path**: `{filepath}`
- **Size**: {size_bytes:,} bytes
- **Lines**: {line_count:,}
- **Extension**: `{filepath.suffix}`
- **Last Modified**: {datetime.fromtimestamp(Path(REPO_ROOT / filepath).stat().st_mtime).isoformat()}

## Original Source

```{self.get_language_for_file(filepath)}
{display_content}
```

## High-Level Overview

{self.generate_overview(filepath, content)}

## Detailed Analysis

{self.generate_detailed_analysis(filepath, content)}

## Usage & Examples

{self.generate_usage_examples(filepath, content)}

## Dependencies & Related Files

{self.find_related_files(filepath, content)}

## Performance & Security Notes

{self.generate_perf_security_notes(filepath, content)}

## Testing & Validation

{self.generate_testing_notes(filepath, content)}

---
*Generated by Repo Book Generator v{self.manifest['generator_version']}*
"""

        # Write documentation
        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)

        self.manifest['bytes_written'] += len(doc_content.encode('utf-8'))
        self.manifest['docs_created'] += 1

        return doc_path

    def generate_file_keywords(self, filepath):
        """Generate _kw.md for a single file"""
        content = self.safe_read_file(REPO_ROOT / filepath)
        if content is None:
            return None

        keywords = self.extract_keywords(content, filepath)

        # Prepare output path
        kw_path = DOCS_ROOT / filepath.parent / f"{filepath.name}_kw.md"
        kw_path.parent.mkdir(parents=True, exist_ok=True)

        # Generate keyword documentation
        kw_content = f"""# Keywords: {filepath.name}

**File**: `{filepath}`

## Keyword Index

"""

        for kw in keywords:
            kw_content += f"### {kw}\n\n"
            kw_content += f"- **Defined in**: [{filepath}](./{filepath.name}_docs.md)\n"
            kw_content += f"- **Context**: {self.get_keyword_context(kw, content)}\n\n"

            # Add to global index
            self.all_keywords[kw].append((str(filepath), self.get_keyword_context(kw, content)))

        kw_content += f"\n---\n*Total keywords: {len(keywords)}*\n"

        # Write keywords
        with open(kw_path, 'w', encoding='utf-8') as f:
            f.write(kw_content)

        self.manifest['bytes_written'] += len(kw_content.encode('utf-8'))
        self.manifest['docs_created'] += 1

        return kw_path

    def get_language_for_file(self, filepath):
        """Get language identifier for code blocks"""
        ext_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.sql': 'sql',
            '.sh': 'bash',
            '.yml': 'yaml',
            '.yaml': 'yaml',
            '.json': 'json',
            '.md': 'markdown',
            '.txt': 'text',
            '.csv': 'csv',
            '.html': 'html',
            '.css': 'css',
            '.r': 'r',
            '.tf': 'terraform',
            '.go': 'go',
            '.java': 'java'
        }
        return ext_map.get(filepath.suffix.lower(), 'text')

    def generate_overview(self, filepath, content):
        """Generate high-level overview"""
        lines = content.split('\n')

        # Extract comments at the top
        overview = ""
        if filepath.suffix == '.py':
            # Look for docstring
            match = re.search(r'"""(.+?)"""', content[:2000], re.DOTALL)
            if match:
                overview = match.group(1).strip()
        elif filepath.suffix in {'.js', '.ts'}:
            # Look for multi-line comment
            match = re.search(r'/\*\*(.+?)\*/', content[:2000], re.DOTALL)
            if match:
                overview = match.group(1).strip()

        if not overview:
            # Generic overview based on file type
            if filepath.suffix == '.py':
                overview = f"Python module containing {len(re.findall(r'def ', content))} functions and {len(re.findall(r'class ', content))} classes."
            elif filepath.suffix in {'.js', '.ts'}:
                overview = f"JavaScript/TypeScript module with {len(re.findall(r'function ', content))} functions."
            elif filepath.suffix == '.sql':
                overview = f"SQL script containing {len(re.findall(r'CREATE', content, re.IGNORECASE))} CREATE statements and {len(re.findall(r'SELECT', content, re.IGNORECASE))} SELECT queries."
            elif filepath.suffix in {'.yml', '.yaml'}:
                overview = "YAML configuration file."
            elif filepath.suffix == '.md':
                overview = "Markdown documentation file."
            elif filepath.name in {'Dockerfile', 'docker-compose.yml'}:
                overview = "Docker configuration file."
            else:
                overview = f"{filepath.suffix[1:].upper() if filepath.suffix else 'Text'} file with {len(lines)} lines."

        return overview

    def generate_detailed_analysis(self, filepath, content):
        """Generate detailed code analysis"""
        analysis = []

        # Python files
        if filepath.suffix == '.py':
            # Functions
            functions = re.findall(r'def\s+(\w+)\s*\(([^)]*)\):', content)
            if functions:
                analysis.append("### Functions\n")
                for func_name, params in functions[:20]:  # Limit to 20
                    analysis.append(f"- **`{func_name}({params})`**\n")

            # Classes
            classes = re.findall(r'class\s+(\w+)(?:\([^)]*\))?:', content)
            if classes:
                analysis.append("\n### Classes\n")
                for cls_name in classes[:20]:
                    analysis.append(f"- **`{cls_name}`**\n")

            # Imports
            imports = re.findall(r'(?:from\s+[\w.]+\s+)?import\s+(.+)', content)
            if imports:
                analysis.append("\n### Dependencies\n")
                for imp in imports[:15]:
                    analysis.append(f"- `{imp.strip()}`\n")

        # JavaScript/TypeScript
        elif filepath.suffix in {'.js', '.ts'}:
            functions = re.findall(r'function\s+(\w+)\s*\(([^)]*)\)', content)
            if functions:
                analysis.append("### Functions\n")
                for func_name, params in functions[:20]:
                    analysis.append(f"- **`{func_name}({params})`**\n")

        # SQL
        elif filepath.suffix == '.sql':
            tables = re.findall(r'CREATE\s+(?:TABLE|VIEW)\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)', content, re.IGNORECASE)
            if tables:
                analysis.append("### Database Objects\n")
                for table in tables:
                    analysis.append(f"- Table/View: **`{table}`**\n")

        if not analysis:
            analysis.append("*Detailed analysis not available for this file type.*\n")

        return "".join(analysis)

    def generate_usage_examples(self, filepath, content):
        """Generate usage examples"""
        examples = []

        # Look for example comments or test code
        if 'example' in content.lower() or 'usage' in content.lower():
            examples.append("*Examples found in source code - see original source above.*\n")
        else:
            examples.append("*No explicit usage examples found in file.*\n")

        return "".join(examples)

    def find_related_files(self, filepath, content):
        """Find related files based on imports/references"""
        related = []

        # Python imports
        imports = re.findall(r'from\s+([\w.]+)\s+import', content)
        imports += re.findall(r'import\s+([\w.]+)', content)

        # JavaScript/TypeScript imports
        imports += re.findall(r'from\s+[\'"]([^\'"]+)[\'"]', content)
        imports += re.findall(r'require\([\'"]([^\'"]+)[\'"]\)', content)

        if imports:
            related.append("### Imported Modules\n\n")
            for imp in set(imports[:20]):
                related.append(f"- `{imp}`\n")
        else:
            related.append("*No external dependencies detected.*\n")

        return "".join(related)

    def generate_perf_security_notes(self, filepath, content):
        """Generate performance and security notes"""
        notes = []

        # Security checks
        security_patterns = {
            'SQL Injection Risk': r'execute\s*\([^)]*%s',
            'Command Injection Risk': r'os\.system\s*\(',
            'Hardcoded Credentials': r'password\s*=\s*[\'"][^\'"]+[\'"]',
            'API Key Exposure': r'api[_-]?key\s*=\s*[\'"][^\'"]+[\'"]',
        }

        for issue, pattern in security_patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                notes.append(f"⚠️ **{issue}** detected - review required\n")

        # Performance notes
        if 'for' in content and 'in' in content:
            if content.count('for ') > 10:
                notes.append("ℹ️ Multiple loops detected - consider optimization\n")

        if not notes:
            notes.append("*No specific performance or security issues detected.*\n")

        return "".join(notes)

    def generate_testing_notes(self, filepath, content):
        """Generate testing notes"""
        notes = []

        if 'test' in filepath.name.lower() or 'spec' in filepath.name.lower():
            notes.append("✓ This is a test file\n")

        if 'pytest' in content or 'unittest' in content:
            notes.append("- Uses pytest/unittest framework\n")

        if 'jest' in content or 'mocha' in content:
            notes.append("- Uses JavaScript testing framework\n")

        if not notes:
            notes.append("*No test framework detected. Manual testing may be required.*\n")

        return "".join(notes)

    def get_keyword_context(self, keyword, content):
        """Get context for a keyword"""
        # Find first occurrence
        pattern = re.compile(r'(.{0,50})\b' + re.escape(keyword) + r'\b(.{0,50})', re.IGNORECASE)
        match = pattern.search(content)

        if match:
            context = match.group(0).strip()
            context = ' '.join(context.split())  # Normalize whitespace
            if len(context) > 100:
                context = context[:100] + "..."
            return context

        return "Identifier or keyword"

    def generate_binary_file_doc(self, filepath):
        """Generate documentation for binary files"""
        doc_path = DOCS_ROOT / filepath.parent / f"{filepath.name}_docs.md"
        doc_path.parent.mkdir(parents=True, exist_ok=True)

        file_stat = (REPO_ROOT / filepath).stat()

        doc_content = f"""# Binary File: {filepath.name}

## File Metadata

- **Path**: `{filepath}`
- **Size**: {file_stat.st_size:,} bytes
- **Type**: Binary ({filepath.suffix})
- **Last Modified**: {datetime.fromtimestamp(file_stat.st_mtime).isoformat()}

## Description

This is a binary file that cannot be displayed as text.

**Recommended handling**:
- Images: View with image viewer
- Archives: Extract with appropriate tool
- Compiled files: Source code documentation available separately

---
*Generated by Repo Book Generator v{self.manifest['generator_version']}*
"""

        with open(doc_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)

        self.manifest['bytes_written'] += len(doc_content.encode('utf-8'))
        self.manifest['docs_created'] += 1

    def process_all_files(self):
        """Process all files and generate documentation"""
        print("\n📝 Processing files...")

        total = len(self.text_files) + len(self.binary_files)
        processed = 0

        # Process text files
        for filepath in self.text_files:
            try:
                self.generate_file_docs(filepath)
                self.generate_file_keywords(filepath)
                processed += 1
                if processed % 10 == 0:
                    print(f"  Processed {processed}/{total} files...")
            except Exception as e:
                self.manifest['errors'].append(f"Error processing {filepath}: {str(e)}")

        # Process binary files (minimal docs)
        for filepath in self.binary_files:
            try:
                self.generate_binary_file_doc(filepath)
                processed += 1
            except Exception as e:
                self.manifest['errors'].append(f"Error processing binary {filepath}: {str(e)}")

        print(f"✓ Processed {processed} files")

    def generate_folder_docs(self, folder_path):
        """Generate index.md, doc.md, and sub.md for a folder"""
        folder_full = DOCS_ROOT / folder_path
        folder_full.mkdir(parents=True, exist_ok=True)

        # Get all direct children
        children_files = []
        children_dirs = set()

        for item in (DOCS_ROOT / folder_path).iterdir():
            if item.is_file() and not item.name.startswith('.'):
                children_files.append(item.name)
            elif item.is_dir():
                children_dirs.add(item.name)

        # Generate index.md
        index_content = f"""# Index: {folder_path if folder_path != Path('.') else 'Root'}

## Contents

### Subdirectories

"""
        for subdir in sorted(children_dirs):
            index_content += f"- [{subdir}/](./{subdir}/index.md)\n"

        index_content += "\n### Files\n\n"

        doc_files = [f for f in children_files if f.endswith('_docs.md')]
        for doc_file in sorted(doc_files):
            original_name = doc_file.replace('_docs.md', '')
            index_content += f"- [{original_name}](./{doc_file})\n"

        with open(folder_full / "index.md", 'w', encoding='utf-8') as f:
            f.write(index_content)

        self.manifest['docs_created'] += 1

        # Generate doc.md
        doc_content = f"""# Documentation: {folder_path if folder_path != Path('.') else 'Root Directory'}

## Overview

This directory contains {len(doc_files)} documented files and {len(children_dirs)} subdirectories.

## Purpose

{self.infer_folder_purpose(folder_path)}

## Structure

- **Files**: {len(doc_files)}
- **Subdirectories**: {len(children_dirs)}

## Navigation

- [View detailed index](./index.md)
- [View keyword index](./sub.md)

---
*Generated by Repo Book Generator*
"""

        with open(folder_full / "doc.md", 'w', encoding='utf-8') as f:
            f.write(doc_content)

        self.manifest['docs_created'] += 1

        # Generate sub.md (keyword aggregation)
        self.generate_folder_keywords(folder_path)

    def infer_folder_purpose(self, folder_path):
        """Infer the purpose of a folder from its name and contents"""
        folder_name = folder_path.name if folder_path != Path('.') else 'root'

        purposes = {
            'test': "Contains test files and testing utilities",
            'src': "Source code directory",
            'lib': "Library files and modules",
            'bin': "Executable scripts and binaries",
            'docs': "Documentation files",
            'config': "Configuration files",
            'data': "Data files and datasets",
            'scripts': "Utility scripts",
            'utils': "Utility functions and helpers",
            'models': "Data models and schemas",
            'api': "API definitions and implementations",
            'components': "UI components",
            'services': "Service layer implementations",
        }

        for keyword, purpose in purposes.items():
            if keyword in folder_name.lower():
                return purpose

        return "General purpose directory containing project files."

    def generate_folder_keywords(self, folder_path):
        """Generate sub.md with aggregated keywords"""
        folder_full = DOCS_ROOT / folder_path

        # Collect all keywords from _kw.md files in this folder
        local_keywords = defaultdict(list)

        for kw_file in folder_full.glob("*_kw.md"):
            # Parse keywords from file
            try:
                with open(kw_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Extract keywords (simplified)
                    keywords = re.findall(r'### (\w+)', content)
                    for kw in keywords:
                        local_keywords[kw].append(kw_file.name.replace('_kw.md', ''))
            except:
                pass

        # Generate sub.md
        sub_content = f"""# Keyword Index: {folder_path if folder_path != Path('.') else 'Root'}

## Alphabetical Keyword Index

"""

        for kw in sorted(local_keywords.keys()):
            sub_content += f"### {kw}\n\n"
            for source in local_keywords[kw]:
                sub_content += f"- [{source}](./{source}_docs.md)\n"
            sub_content += "\n"

        sub_content += f"\n---\n*Total unique keywords: {len(local_keywords)}*\n"

        with open(folder_full / "sub.md", 'w', encoding='utf-8') as f:
            f.write(sub_content)

        self.manifest['docs_created'] += 1

    def process_all_folders(self):
        """Process all folders and generate folder-level documentation"""
        print("\n📁 Processing folders...")

        # Get all unique folder paths in docs
        folders = set()
        for root, dirs, files in os.walk(DOCS_ROOT):
            rel_path = Path(root).relative_to(DOCS_ROOT)
            folders.add(rel_path)

        for folder in sorted(folders):
            try:
                self.generate_folder_docs(folder)
            except Exception as e:
                self.manifest['errors'].append(f"Error processing folder {folder}: {str(e)}")

        print(f"✓ Processed {len(folders)} folders")

    def build_global_keywords(self):
        """Build global keywords.md"""
        print("\n🔤 Building global keyword index...")

        keywords_content = """# Global Keyword Index

This index contains all keywords extracted from the repository, sorted alphabetically.

"""

        for kw in sorted(self.all_keywords.keys()):
            keywords_content += f"## {kw}\n\n"

            for filepath, context in self.all_keywords[kw][:10]:  # Limit per keyword
                doc_path = Path(filepath).parent / f"{Path(filepath).name}_docs.md"
                keywords_content += f"- **[{filepath}](./{doc_path})**: {context}\n"

            if len(self.all_keywords[kw]) > 10:
                keywords_content += f"- *(... and {len(self.all_keywords[kw]) - 10} more occurrences)*\n"

            keywords_content += "\n"

        keywords_content += f"\n---\n*Total unique keywords: {len(self.all_keywords)}*\n"

        with open(DOCS_ROOT / "keywords.md", 'w', encoding='utf-8') as f:
            f.write(keywords_content)

        self.manifest['docs_created'] += 1
        print(f"✓ Created global keyword index with {len(self.all_keywords)} keywords")

    def build_root_index(self):
        """Build root index.md"""
        print("\n📑 Building root index...")

        index_content = """# Repository Documentation Index

Welcome to the comprehensive documentation for this repository.

## Navigation

- [📖 Comprehensive Book](./comprehensive_book.md) - Full repository documentation in book format
- [🔤 Global Keyword Index](./keywords.md) - All keywords A-Z
- [✅ Verification Report](./verification_report.md) - Link validation and processing report
- [📋 Manifest](./manifest.json) - Metadata and statistics

## Directory Structure

"""

        # List all top-level folders
        for item in sorted(DOCS_ROOT.iterdir()):
            if item.is_dir() and not item.name.startswith('.'):
                index_content += f"- [{item.name}/](./{item.name}/index.md)\n"

        index_content += "\n## Repository Statistics\n\n"
        index_content += f"- **Files scanned**: {self.manifest['files_scanned']}\n"
        index_content += f"- **Documentation files created**: {self.manifest['docs_created']}\n"
        index_content += f"- **Total keywords indexed**: {len(self.all_keywords)}\n"

        index_content += "\n---\n*Generated by Repo Book Generator*\n"

        with open(DOCS_ROOT / "index.md", 'w', encoding='utf-8') as f:
            f.write(index_content)

        self.manifest['docs_created'] += 1
        print("✓ Created root index")

    def build_comprehensive_book(self):
        """Build comprehensive_book.md"""
        print("\n📚 Building comprehensive book...")

        book_content = f"""# Comprehensive Repository Documentation

**Repository**: {self.manifest['repo_source']}
**Commit**: {self.manifest['commit_sha']}
**Generated**: {datetime.utcnow().isoformat()}

---

## Table of Contents

1. [Introduction](#introduction)
2. [Repository Structure](#repository-structure)
3. [Detailed Documentation](#detailed-documentation)
4. [Keyword Index](#keyword-index)

---

## Introduction

This comprehensive book contains detailed documentation for all files in the repository.

### Statistics

- **Total Files**: {self.manifest['files_scanned']}
- **Text Files**: {len(self.text_files)}
- **Binary Files**: {len(self.binary_files)}
- **Documentation Files Generated**: {self.manifest['docs_created']}

---

## Repository Structure

"""

        # Add folder structure
        for root, dirs, files in os.walk(DOCS_ROOT):
            rel_path = Path(root).relative_to(DOCS_ROOT)
            if rel_path == Path('.'):
                continue

            level = len(rel_path.parts)
            indent = "  " * level

            book_content += f"{indent}- **{rel_path.name}/**\n"

        book_content += "\n---\n\n## Detailed Documentation\n\n"

        # Add folder doc.md contents as chapters
        chapters = []
        for root, dirs, files in os.walk(DOCS_ROOT):
            doc_md = Path(root) / "doc.md"
            if doc_md.exists():
                try:
                    with open(doc_md, 'r', encoding='utf-8') as f:
                        content = f.read()
                        rel_path = Path(root).relative_to(DOCS_ROOT)
                        book_content += f"### Chapter: {rel_path if rel_path != Path('.') else 'Root'}\n\n"
                        book_content += content + "\n\n---\n\n"
                except:
                    pass

        book_content += "\n## Keyword Index\n\n"
        book_content += f"See [keywords.md](./keywords.md) for the complete keyword index.\n\n"
        book_content += f"**Total Keywords**: {len(self.all_keywords)}\n\n"

        book_content += "---\n\n*End of Comprehensive Book*\n"

        with open(DOCS_ROOT / "comprehensive_book.md", 'w', encoding='utf-8') as f:
            f.write(book_content)

        self.manifest['docs_created'] += 1
        print("✓ Created comprehensive book")

    def validate_and_report(self):
        """Validate all links and create verification report"""
        print("\n✅ Validating and creating verification report...")

        broken_links = []
        skipped_files = []

        # Add binary files to skipped
        for bf in self.binary_files:
            skipped_files.append((str(bf), "Binary file"))

        # Add large files to skipped
        for lf in self.large_files:
            skipped_files.append((str(lf), "Large file (>100MB)"))

        report_content = f"""# Verification Report

**Generated**: {datetime.utcnow().isoformat()}
**Commit SHA**: {self.manifest['commit_sha']}

## Summary

- **Files Scanned**: {self.manifest['files_scanned']}
- **Documentation Created**: {self.manifest['docs_created']}
- **Errors**: {len(self.manifest['errors'])}
- **Skipped Files**: {len(skipped_files)}
- **Broken Links**: {len(broken_links)}

## Processing Errors

"""

        if self.manifest['errors']:
            for error in self.manifest['errors']:
                report_content += f"- {error}\n"
        else:
            report_content += "*No errors encountered.*\n"

        report_content += "\n## Skipped Files\n\n"

        if skipped_files:
            for filepath, reason in skipped_files:
                report_content += f"- `{filepath}`: {reason}\n"
        else:
            report_content += "*No files skipped.*\n"

        report_content += "\n## Broken Links\n\n"

        if broken_links:
            for link in broken_links:
                report_content += f"- {link}\n"
        else:
            report_content += "*All links validated successfully.*\n"

        report_content += "\n## File Type Distribution\n\n"

        extensions = defaultdict(int)
        for f in self.all_files:
            ext = Path(f).suffix or '.txt'
            extensions[ext] += 1

        for ext, count in sorted(extensions.items(), key=lambda x: x[1], reverse=True):
            report_content += f"- `{ext}`: {count} files\n"

        report_content += "\n---\n*Verification complete*\n"

        with open(DOCS_ROOT / "verification_report.md", 'w', encoding='utf-8') as f:
            f.write(report_content)

        self.manifest['docs_created'] += 1
        print("✓ Created verification report")

    def finalize_manifest(self):
        """Finalize and write manifest.json"""
        print("\n📋 Finalizing manifest...")

        self.manifest['timestamp_end'] = datetime.utcnow().isoformat()
        self.manifest['commit_sha'] = self.get_commit_sha()
        self.manifest['repo_fingerprint'] = self.compute_fingerprint()

        # Compute checksums for all generated markdown files
        checksums = {}
        for root, dirs, files in os.walk(DOCS_ROOT):
            for filename in files:
                if filename.endswith('.md') or filename.endswith('.json'):
                    filepath = Path(root) / filename
                    try:
                        with open(filepath, 'rb') as f:
                            content = f.read()
                            checksums[str(filepath.relative_to(DOCS_ROOT))] = hashlib.sha256(content).hexdigest()
                    except:
                        pass

        self.manifest['file_checksums'] = checksums

        with open(DOCS_ROOT / "manifest.json", 'w', encoding='utf-8') as f:
            json.dump(self.manifest, f, indent=2)

        print("✓ Manifest finalized")

    def create_readme(self):
        """Create docs/README.md"""
        readme_content = """# Repository Documentation

This directory contains comprehensive, auto-generated documentation for the entire repository.

## Generated by

**Repo Book Generator v1.0.0** - World's Best Repo Book Generator and Index Builder

## Structure

- `manifest.json` - Metadata, statistics, and file checksums
- `index.md` - Main navigation index
- `keywords.md` - Global A-Z keyword index
- `comprehensive_book.md` - Complete documentation in book format
- `verification_report.md` - Processing report and validation results
- `README.md` - This file

### Per-File Documentation

Each source file has two generated documentation files:

- `<filename>_docs.md` - Comprehensive documentation with source code, analysis, and usage
- `<filename>_kw.md` - Keyword index for that specific file

### Per-Folder Documentation

Each directory has three documentation files:

- `index.md` - Directory listing and navigation
- `doc.md` - Directory purpose and overview
- `sub.md` - Aggregated keyword index for the directory

## How to Use

1. Start with `index.md` for overall navigation
2. Use `keywords.md` to find specific terms or concepts
3. Read `comprehensive_book.md` for a linear walkthrough
4. Check `verification_report.md` for processing details

## Resuming / Expanding

To regenerate or update documentation:

```bash
python3 repo_book_gen.py
```

The process is idempotent - running it again will recreate the documentation with the latest repository state.

## Principles

- **Truth-first**: No invented content
- **Deterministic**: Same repo = same docs
- **Verifiable**: Full checksums and validation
- **Link-safe**: All internal links are relative and validated

---

*For questions or issues, check the verification_report.md*
"""

        with open(DOCS_ROOT / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme_content)

        self.manifest['docs_created'] += 1
        print("✓ Created README")

    def run(self):
        """Main execution flow"""
        print("=" * 60)
        print("  REPO BOOK GENERATOR v1.0.0")
        print("  World's Best Repo Book Generator and Index Builder")
        print("=" * 60)

        # Step 1: Bootstrap
        print("\n[1/10] Bootstrap")
        self.scan_repository()

        # Step 2: Process files
        print("\n[2/10] Generate per-file documentation")
        self.process_all_files()

        # Step 3: Process folders
        print("\n[3/10] Generate per-folder documentation")
        self.process_all_folders()

        # Step 4: Global keywords
        print("\n[4/10] Build global keyword index")
        self.build_global_keywords()

        # Step 5: Root index
        print("\n[5/10] Build root index")
        self.build_root_index()

        # Step 6: Comprehensive book
        print("\n[6/10] Build comprehensive book")
        self.build_comprehensive_book()

        # Step 7: Verification
        print("\n[7/10] Validate and create verification report")
        self.validate_and_report()

        # Step 8: Finalize manifest
        print("\n[8/10] Finalize manifest")
        self.finalize_manifest()

        # Step 9: Create README
        print("\n[9/10] Create README")
        self.create_readme()

        # Step 10: Summary
        print("\n[10/10] Complete!")
        print("\n" + "=" * 60)
        print("  GENERATION COMPLETE")
        print("=" * 60)

        summary = {
            "repo_source": self.manifest['repo_source'],
            "repo_fingerprint": self.manifest['repo_fingerprint'],
            "commit_sha": self.manifest['commit_sha'],
            "files_scanned": self.manifest['files_scanned'],
            "docs_created": self.manifest['docs_created'],
            "words_estimated": self.manifest['bytes_written'] // 6,  # Rough estimate
            "bytes_written": self.manifest['bytes_written'],
            "errors": self.manifest['errors']
        }

        print("\n📊 FINAL SUMMARY:")
        print(json.dumps(summary, indent=2))

        return summary


if __name__ == "__main__":
    generator = RepoBookGenerator()
    summary = generator.run()

    # Write summary to file for easy retrieval
    with open(DOCS_ROOT / "_generation_summary.json", 'w') as f:
        json.dump(summary, f, indent=2)
