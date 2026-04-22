name: Build AL-HISN 26 APK
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Buildozer dependencies
        run: |
          sudo apt update
          sudo apt install -y git zip unzip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
          pip install --user --upgrade buildozer cython virtualenv

      - name: Build with Buildozer
        run: |
          yes | buildozer -v android debug
        continue-on-error: false

      - name: Upload APK
        uses: actions/setup-node@v4 # لضمان توافق البيئة
      
      - name: Final Step - Upload Artifact
        uses: actions/upload-artifact@v4 # هنا التحديث الهام لنسخة v4
        with:
          name: Al-Hisn-Game-APK
          path: bin/*.apk
          
