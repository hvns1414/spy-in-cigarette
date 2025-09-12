@echo off

REM Kullanıcıdan yönetici izni almak için
echo Yükleme işlemi başlatılıyor...

REM Python 3'ün yüklü olup olmadığını kontrol et
python --version >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python 3 yüklü değil. Lütfen Python 3'ü yükleyin.
    exit /b
)

REM Pip'in yüklü olup olmadığını kontrol et
pip --version >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Pip yüklü değil. Pip'i yüklemek için Python ile birlikte yüklemeniz gerekir.
    exit /b
)

REM Gerekli bağımlılıkları yükle
echo Bağımlılıklar yükleniyor...
pip install -r requirements.txt

REM Yükleme tamamlandı
echo Yükleme tamamlandı! Artık scripti çalıştırabilirsiniz.
echo Ornek kullanım: python script.py -l

pause
