# Keywords: repo_book_gen.py

**File**: `repo_book_gen.py`

## Keyword Index

### Path

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: from pathlib import Path

### RepoBookGenerator

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: class RepoBookGenerator:

### __init__

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def __init__(self):

### _kw

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: """Generate _kw.md for a single file"""

### build_comprehensive_book

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def build_comprehensive_book(self):

### build_global_keywords

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def build_global_keywords(self):

### build_root_index

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def build_root_index(self):

### collections

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: from collections import defaultdict

### compute_fingerprint

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def compute_fingerprint(self):

### content

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: content = "\n".join(file_list)

### create_readme

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def create_readme(self):

### datetime

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: from datetime import datetime

### defaultdict

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: from collections import defaultdict

### extract_keywords

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def extract_keywords(self, content, filepath):

### file

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: .all_keywords = defaultdict(list) # keyword -> [(file, description)]

### finalize_manifest

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def finalize_manifest(self):

### find_related_files

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: {self.find_related_files(filepath, content)}

### generate_binary_file_doc

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def generate_binary_file_doc(self, filepath):

### generate_detailed_analysis

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: {self.generate_detailed_analysis(filepath, content)}

### generate_file_docs

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def generate_file_docs(self, filepath):

### generate_file_keywords

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def generate_file_keywords(self, filepath):

### generate_folder_docs

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def generate_folder_docs(self, folder_path):

### generate_folder_keywords

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: self.generate_folder_keywords(folder_path)

### generate_overview

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: {self.generate_overview(filepath, content)}

### generate_perf_security_notes

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: {self.generate_perf_security_notes(filepath, content)}

### generate_testing_notes

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: {self.generate_testing_notes(filepath, content)}

### generate_usage_examples

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: {self.generate_usage_examples(filepath, content)}

### get_commit_sha

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def get_commit_sha(self):

### get_keyword_context

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: kw_content += f"- **Context**: {self.get_keyword_context(kw, content)}\n\n"

### get_language_for_file

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: ```{self.get_language_for_file(filepath)}

### hashlib

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: import hashlib

### infer_folder_purpose

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: {self.infer_folder_purpose(folder_path)}

### is_binary_file

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def is_binary_file(self, filepath):

### its

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: """Infer the purpose of a folder from its name and contents"""

### json

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: import json

### mimetypes

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: import mimetypes

### pathlib

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: from pathlib import Path

### process_all_files

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def process_all_files(self):

### process_all_folders

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def process_all_folders(self):

### run

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: result = subprocess.run(['git', 'rev-parse', 'HEAD'],

### safe_read_file

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def safe_read_file(self, filepath):

### scan_repository

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def scan_repository(self):

### subprocess

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: import subprocess

### sys

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: import sys

### validate_and_report

- **Defined in**: [repo_book_gen.py](./repo_book_gen.py_docs.md)
- **Context**: def validate_and_report(self):


---
*Total keywords: 45*
