#!/bin/bash

# Kullanıcıdan sudo şifresi istemek
echo "Yükleme işlemi başlatılıyor..."

# Python ve pip'in yüklü olduğundan emin olalım
if ! command -v python3 &> /dev/null
then
    echo "Python 3 yüklü değil. Lütfen Python 3'ü yükleyin."
    exit
fi

if ! command -v pip3 &> /dev/null
then
    echo "Pip yüklü değil. Pip'i yüklemek için 'sudo apt install python3-pip' komutunu çalıştırın."
    exit
fi

# Gerekli bağımlılıkları yükleyelim
echo "Bağımlılıklar yükleniyor..."
pip3 install -r requirements.txt

# Yükleme tamamlandı
echo "Yükleme tamamlandı! Artık scripti çalıştırabilirsiniz."
echo "Örnek kullanım: python3 script.py -l"

