import os, zipfile
from pathlib import Path

class MCLib:
    """마인크래프트 관련 함수들을 모아둔 클래스입니다"""

    """
        *Pack Format Table*
        1.13-1.14.4: 4
        1.15-1.16.1: 5
        1.16.2-1.16.5: 6
        1.17-1.17.1: 7
        1.18-1.18.1: 8
        1.18.2: 9
        1.19-1.19.3: 10
        1.19.4-: 11
    """
    version_dict = { 
        "1.13": 4, "1.13.1": 4, "1.13.2": 4,
        "1.14": 4, "1.14.1": 4, "1.14.2": 4, "1.14.3": 4, "1.14.4": 4,

        "1.15": 5, "1.15.1": 5, "1.15.2": 5,
        "1.16": 5, "1.16.1": 5,

        "1.16.2": 6, "1.16.3": 6, "1.16.4": 6, "1.16.5": 6,
        "1.17": 7, "1.17.1": 7,
        "1.18": 8, "1.18.1": 8,
        "1.18.2": 9,

        "1.19": 10, "1.19.1": 10, "1.19.2": 10, "1.19.3": 10,
        "1.19.4": 11, "1.20": 11
    }
    
    @staticmethod
    def convert_version(version: str) -> int:
        """MC Version을 Pack Format으로 변환합니다

        Args:
            version (str): MC Version

        Returns:
            int: Pack Format
        """        
        return MCLib.version_dict[version]

class FileLib:
    @staticmethod
    def zip_dir(directory: str, target: str):
        zip_file = zipfile.ZipFile(target, "w")

        working_directory = os.getcwd()
        current_path = os.path.join(working_directory, directory)
        for (path, dir, files) in os.walk(current_path):
            for file in files:
                zip_file.write(os.path.join(path, file), compress_type=zipfile.ZIP_DEFLATED)

        zip_file.close()

    @staticmethod
    def regenerate_dir(target: str) -> Path:
        target_path = Path(target)

        if not target_path.is_file():
            target_path.mkdir(exist_ok=True)
        else:
            target_path.unlink(missing_ok=True)
            target_path.mkdir()

        return target_path