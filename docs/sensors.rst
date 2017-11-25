Sensory
=======

:Dane z sensorów: http://icares1.habitatos.space/sensors/zwavesensor/
:Wykres temperatury: http://icares1.habitatos.space/api/v1/sensor/chart/temperature/
:Wykres wilgotności: http://icares1.habitatos.space/api/v1/sensor/chart/relative-humidity/

Instalacja skryptów na urządzeniu
---------------------------------
.. code-block: console

        $ PYTHON_VERSION=3.6.3

        $ apt-get install sqlite3 libsqlite3-dev libssl-dev vim
        $ cd /usr/src
        $ curl https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz -o python.tgz
        $ tar zxf python.tgz
        $ cd python-*
        $ ./configure
        $ make -j 4
        $ sudo make install



Rozwiązywanie problemów
-----------------------

Brak aktualizacji temperatury
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Jeżeli na stronie http://icares1.habitatos.space/sensors/zwavesensor/ nie pojawiają się nowe dane, to przyczyną może być:

- brak prądu, lub wyłączone urządzenie *Raspberry PI* (192.168.255.11)
- brak połączenia sieciowego z internetem (padła sieć w habitacie)
- zablokowany ruch sieciowy na *.habitatos.space
- problem z urządzeniem *Raspberry PI* (192.168.255.11), który zbiera dane
- błąd karty SD na której *Raspberry PI* zapisuje dane (czasami się uszkadza przy gwałtownym
- problem z bazą Z-Wave, które jest podpięte do *Raspberry PI* (192.168.255.11)
- problem z czujnikami

Aby zdiagnozować problem, połącz się z *Raspberry PI*:

.. code-block:: console

    $ ssh pi@192.168.255.11 -p 22
    # hasło standardowe jak w habitacie zaczynające się od dużej litery U...

Jeżeli host nie odpowiada, to może mieć inne IP. Przeskanuj sieć wykorzystując program ``nmap`` (https://nmap.org/download.html).

Przeskanuj komputery w sieci 192.168.255.0/24 wyłącznie na portach 22 wykorzystując opcję zwracającą wersję usługi (``-sV``):

.. code-block:: console

    $ nmap 192.168.255.0/24 -sV -p 22

Jeżeli korzystasz z opcji graficznej (``Zenmap``) to wynik powinien wyglądać tak:

.. code-block:: console

    Starting Nmap 7.60 ( https://nmap.org ) at 2017-11-24 18:02 CET.
    Nmap scan report for homerouter.cpe (192.168.255.1)
    Host is up (0.00s latency).
    MAC Address: AC:CF:85:79:3F:49 (Huawei Technologies)
    Nmap scan report for 192.168.255.11
    Host is up (0.015s latency).
    MAC Address: B8:27:EB:2A:34:95 (Raspberry Pi Foundation)
    Nmap scan report for 192.168.255.19
    Host is up (0.093s latency).
    MAC Address: 08:11:96:41:2A:14 (Intel Corporate)
    Nmap scan report for 192.168.255.20
    Host is up (0.015s latency).
    MAC Address: 80:86:F2:16:D9:06 (Intel Corporate)
    Nmap scan report for 192.168.255.21
    Host is up (0.015s latency).
    MAC Address: 98:F0:AB:47:A3:7C (Apple)
    Nmap scan report for 192.168.255.201
    Host is up (0.00s latency).
    MAC Address: B8:27:EB:2A:34:95 (Raspberry Pi Foundation)
    Nmap scan report for 192.168.255.15
    Host is up.
    Nmap done: 256 IP addresses (7 hosts up) scanned in 3.62 seconds

.. hint:: Jak to czytać?
    Nowa linia zaczyna się od słówka MAC Address, a w następnej linii jest adres IP, którego szukamy

    .. code-block:: console

        Starting Nmap 7.60 ( https://nmap.org ) at 2017-11-24 18:02 CET.

        Nmap scan report for homerouter.cpe (192.168.255.1)
        Host is up (0.00s latency).

        MAC Address: AC:CF:85:79:3F:49 (Huawei Technologies)
        Nmap scan report for 192.168.255.11
        Host is up (0.015s latency).

        MAC Address: B8:27:EB:2A:34:95 (Raspberry Pi Foundation)
        Nmap scan report for 192.168.255.19
        Host is up (0.093s latency).

        MAC Address: 08:11:96:41:2A:14 (Intel Corporate)
        Nmap scan report for 192.168.255.20
        Host is up (0.015s latency).

        MAC Address: 80:86:F2:16:D9:06 (Intel Corporate)
        Nmap scan report for 192.168.255.21
        Host is up (0.015s latency).

        MAC Address: 98:F0:AB:47:A3:7C (Apple)
        Nmap scan report for 192.168.255.201
        Host is up (0.00s latency).

        MAC Address: B8:27:EB:2A:34:95 (Raspberry Pi Foundation)
        Nmap scan report for 192.168.255.15
        Host is up.

        Nmap done: 256 IP addresses (7 hosts up) scanned in 3.62 seconds

Lepiej, możesz wykorzystać ``grep`` aby przefiltrować wyniki:

.. code-block:: console

    $ nmap 192.168.255.0/24 -sV -p 22 |grep -i Raspberry -A 1

    MAC Address: B8:27:EB:2A:34:95 (Raspberry Pi Foundation)
    Nmap scan report for 192.168.255.19
    --
    MAC Address: B8:27:EB:2A:34:95 (Raspberry Pi Foundation)
    Nmap scan report for 192.168.255.15

Jeden z nich powinien zwrócić adres naszego urządzenia.

.. note:: Jeżeli nie wyświetla się żadne urządzenie:

    - mamy problem z urządzeniem (fizycznie uszkodzone)
    - jest problem z kartą SD (trzeba sfromatować i ponownie wgrać)
    - jest problem z siecią w habitacie
    - urządzenie nie ma przydzielonego IP (serwer DHCP nie działał jak było restartowane)

Następnie trzeba się połączyć z urządzeniem wykorzystując SSH (na Windows skorzystaj z PuTTY http://www.putty.org/)

.. code-block:: console

    $ ssh pi@ADRES_IP
    # hasło standardowe jak w habitacie (zaczynające się od dużej litery U...)

Po zalogowaniu wykonaj polecenie:

.. code-block:: console

    $ ps aux |grep sensor

    (virtualenv-3.6.3) pi@hab:~ $ ps aux | grep sensor
    pi         626  1.0  1.8  50172 17548 ?        Sl   17:18   0:02 /home/pi/virtualenv-3.6.3/bin/python3 /home/pi/lunares_hab/sensor-zwave-collector.py
    pi        1046  0.0  0.0   2672   568 pts/0    S+   17:21   0:00 grep --color=auto sensor

Wynik powinien zawierać jeden proces. Czasami w wynikach pojawia się dodatkow linijka ``grep --color=auto sensor`` ale nas to nie interesuje.
Jeżeli proces jest uruchomiony to dane się zbierają i zapisują do lokalnej bazy danych *SQLite 3* (``/home/pi/lunares_hab/sensor-data.sqlite3``).
Możesz to zweryfikować wykonując polecenie:

.. code-block:: console

    sqlite3 /home/pi/lunares_hab/sensor-data.sqlite3 'SELECT * FROM sensor_data ORDER BY datetime DESC LIMIT 30'

Jeżeli nie jest obecny proces zbierający dane, to jego uruchomienie można wymusić wykonując polecenie:

.. code-block:: console

    $ /etc/init.d/HABITAT-zwave-extract start

Proces powinien się uruchamiać automatycznie przy restarcie urządzenia, więc alternatywnie można odłączyć urządzenie od prądu i podłączyć ponownie.

.. warning:: Raspberry PI zapisuje dużo danych na karcie SD i jeżeli podczas zapisu nastąpi wyłączenie prądu, to może to uszkodzić kartę i urządzenie ponownie się nie włączy do czasu sformatowania karty i ponownego wgrania systemu operacyjnego!

Dla pewności można wykonać polecenie, które pokaże czy skrypt uploadujący dane do *habitatOS* jest uruchomiony.

.. code-block:: console

    $ crontab -l
    */2 * * * * /home/pi/virtualenv-3.6.3/bin/python3 /home/pi/lunares_hab/sensor-zwave-uploader.py 1>/dev/null
