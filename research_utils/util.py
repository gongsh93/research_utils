import os
import glob
from typing import List, Dict

def find_target_files(directories: List[str], extensions: List[str]) -> Dict[str, List[str]]:
    """
    Search for files with given extensions in multiple directories.

    Args:
        directories (List[str]): List of absolute directory paths to search.
        extensions (List[str]): List of file extensions to look for (e.g., ['.csv', '.txt']).

    Returns:
        Dict[str, List[str]]: Dictionary where keys are extensions and values are lists of matching file paths.
    """
    found_files = {ext: [] for ext in extensions}
    
    for directory in directories:
        if not os.path.isdir(directory):    # Validate directory existence
            print(f"Warning: {directory} is not a valid directory.")
            continue
        
        for ext in extensions:
            search_pattern = os.path.join(directory, f"**/*{ext}")  # Recursive search pattern
            matched_files = glob.glob(search_pattern, recursive=True) # Find matching files
            found_files[ext].extend(matched_files)
        
        return found_files