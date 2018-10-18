# PythonMyFirstSteps

Проект тестовый для изучения Python (Для Ильдуса)

работает на python2.7

нужно установить библиотеку
sudo apt-get update
sudo apt-get install python-qrtools

при работе с библиотекой могут возникнуть проблемы
    Traceback (most recent call last):
      File "qrtoolsT2.py", line 7, in <module>
        my_QR.decode()
      File "/usr/lib/python2.7/dist-packages/qrtools.py", line 181, in decode
        raw = pil.tostring()
      File "/usr/lib/python2.7/dist-packages/PIL/Image.py", line 695, in tostring
        "Please call tobytes() instead.")
Exception: tostring() has been removed. Please call tobytes() instead.
ну соответсвенно в данной ситуации я подредактировал файл /usr/lib/python2.7/dist-packages/qrtools.py на линии 181 tostring() на tobytes()

# qrtoolsT1.py
создает кр код и помещает в текущую папку.
# qrtoolsT2.py
считывает кр код и показывает раскодированный текст.
# qrtoolsT3.py
создает кр код с большим разрешение и помещает в текущую папку.
