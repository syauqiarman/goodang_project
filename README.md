# **Goodang**

**Syauqi Armanaya Syaki**<br/>
**2206829010**<br/>
**PBP D**<br/>

Dapat diakses melalui link [Goodang](https://goodang.adaptable.app/main/).
<br/>
<br/>

# **Tugas 2 - Implementasi Model-View-Template (MVT) pada Django**
Mengimplementasikan konsep Model-View-Template (MVT) pada Django dan konsep lainnya yang sudah dipelajari di kelas, serta menjawab beberapa pertanyaan.

## **Membuat sebuah proyek Django baru**
1. Buat direktori lokal baru dengan nama yang diinginkan, contohnya `example_project` selanjutnya masuk ke dalam direktori tersebut dan buka *command prompt* (Windows) atau *terminal shell* (Unix).
2. Buat *virtual environment* untuk mengisolasi proyek kita dengan perintah `python -m venv env`.
3. Aktifkan *virtual environment* dengan cara `env\Scripts\activate.bat` untuk Windows dan `source env/bin/activate` untuk Unix (Mac/Linux).

**NOTE:** Pastikan *virtual environment* sudah aktif yang ditandai dengan `(env)` di baris input terminal

4. Buat file txt dengan nama `requirements.txt` di dalam direktori yang sama dan tambahkan beberapa *dependencies* ke dalamnya.
```txt
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
5. Install *dependencies* yang sudah dimasukkan ke `requirements.txt` dengan menjalankan perintah `pip install -r requirements.txt`.
6. Buat proyek Django dengan nama yang diinginkan (saya menggunakan nama `goodang`) dengan perintah berikut. `django-admin startproject goodang .`

**NOTE:** Pastikan karakter `.` ditulis di akhir perintah

7. Buka `settings.py` lalu dibagian `ALLOWED_HOSTS` tambahkan `*` agar aplikasi dapat diakses semua host.
```python
...
ALLOWED_HOSTS = ["*"]
...
```
8. Jalankan server Django dengan perintah `python manage.py runserver` (Windows) atau `./manage.py runserver` (Unix). Pastikan ada file `manage.py` di direktori yang digunakan.
9. Buka http://localhost:8000 di web, jika terlihat animasi roket maka aplikasi Django berhasil dibuat.
10. Untuk menghentikan server, tekan `Ctrl+C` (Windows/Linux) atau `Control+C` (Mac) pada *shell*. Matikan *virtual environtment* dengan perintah `deactivate`

## **Membuat Aplikasi `main` dalam Proyek**
1. Jalankan perintah berikut di terminal atau *command prompt* yang dibuka dari direktori lokal. `python manage.py startapp main`
2. Buka `settings.py` untuk menambahkan ``main`` ke dalam daftar aplikasi.
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
## **Membuat `main.html`**
1. Buat direktori baru bernama `templates` di dalam direktori aplikasi main.
2. Buat file bernama `main.html` di dalam direktori `templates`.

## **Mengubah file `models.py` dalam `main`**
1. Buka file `models.py` dan isi dengan kode berikut.
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
```
**Penjelasan Kode:**
* `name` sebagai nama item yang tipenya `CharField`.
* `amount` sebagai jumlah item tipenya `IntegerField`.
* `description` sebagai deskripsi item yang tipenya `TextField`.
* `price` sebagai jumlah item tipenya `IntegerField`.
* `category` sebagai nama item yang tipenya `CharField`.
* `date_added` sebagai nama item yang tipenya `DateField`.
Bebas untuk menambahkan atribut lainnya jika diinginkan.
2. Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk melakukan migrasi pada Django.

> [!IMPORTANT]
> Setiap melakukan perubahan pada `models.py`, perlu melakukan migrasi untuk merefleksikan perubahan tersebut.

## **Menghubungkan `View` dengan `Template`**
1. Buka file `views.py` dan tambahkan baris berikut.
```python
from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Kaos hitam polos',
        'amount': 20,
        'description':'Kaos polos pria berbahan Cotton Combed 30s round neck reguler fit',
        'price': 50000,
        'category': 'fashion pria'
    }

    return render(request, "main.html", context)
```
**Penjelasan Kode:**
* Import yang dilakukan dapat berguna untuk mengimpor fungsi *render* dari modul `django.shortcuts` yang digunakan untuk memproses tampilan HTML dengan data yang ada.
* Fungsi `show_main` berfungsi untuk mengatur permintaan HTTP dan mengembalikan tampilan yang tepat.
* `context` digunakan untuk mengirimkan data ke tampilan.
* `return render(request, "main.html", context)` digunakan untuk melakukan *rendering* tampilan `main.html` dengan menggunakan fungsi `render`yang memiliki argumen `request` sebagai objek permintaan HTTP dari *user*, `main.html` sebagai berkas template yang akan digunakan, dan `context` sebagai dictionary yang berisi data yang akan digunakan.

## **Memodifikasi template**
1. Buka file `main.html` yang sudah dibuat sebelumnya, dan isi dengan data yang akan kamu gunakan, contohnya:
```html
<h1>Goodang Page</h1>

<h5>Name: Syauqi Armanaya Syaki</h5>
<h5>Class: PBP D</h5>
<h5>ITEM: </h5>
<h5>Name: </h5>
<p>{{ name }}</p> <!-- Ubahlah sesuai dengan nama produk -->
<h5>Amount: </h5>
<p>{{ amount }}</p> <!-- Ubahlah sesuai dengan jumlah produk -->
<h5>Description: </h5>
<p>{{ description }}</p> <!-- Ubahlah sesuai dengan deskripsi produk -->
<h5>Price: </h5>
<p>{{ price }}</p> <!-- Ubahlah sesuai dengan harga produk -->
<h5>Category: </h5>
<p>{{ category }}</p> <!-- Ubahlah sesuai dengan harga produk -->
```
**Penjelasan Kode:**
* sintaks `{{}}` digunakan untuk menampilkan data yang telah didefinisikan di `context`.
* `main.html` diatas hanyalah contoh dan bisa dikembangkan.

## **Konfigurasi Routing URL**
1. Buat berkas `urls.py` di dalam direktori `main`, lalu isi dengan kode berikut.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
2. Buka file `urls.py` di dalam direktori proyek (disini direktori saya bernama `goodang`), bukan yang di dalam direktori `main`. Lalu tambahkan impor berikut.
```python
...
from django.urls import path, include
...
```
3. Selanjutnya tambahkan rute url seperti berikut.
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```

## **Unit Testing**
1. Buka file `test.py` pada direktori `main`. Lalu isi dengan kode berikut.
```python
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_item_details(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Kaos hitam polos')
        self.assertContains(response, 20) 
        self.assertContains(response, 'Kaos polos pria berbahan Cotton Combed 30s round neck reguler fit') 
        self.assertContains(response, 50000) 
        self.assertContains(response, 'fashion pria')
```
**Penjelasan Kode:**
* `test_main_url_is_exist` adalah untuk mengecek apakah *path* `/main/` bisa diakses.
* `test_main_using_main_template` adalah untuk mengecek halaman `/main/` me *render* dengan *template* `main.html`.
* `test_item_details` adalah untuk mengecek kesesuaian isi dari variabel yang sudah dibuat.
2. Jalankan dengan perintah `python manage.py test`. Jika berhasil maka akan keluar seperti berikut.
```txt
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.025s

OK
Destroying test database for alias 'default'...
```

## **Membuat dan mengunggah proyek ke Github**
1. Di dalam direktori yang sudah dibuat, buka *command prompt* (Windows) atau *terminal shell* (Unix). Lalu inisiasi repositori baru dengan perintah `git init`.
2. Lakukan konfigurasi *username* dengan perintah `git config user.name "<NAME>"` dan *email* dengan perintah `git config user.email "<EMAIL>"` yang akan dihubungkan dengan proyekmu ke repositori Git. (*username* dan *email* disesuaikan dengan Github mu). Lalu pastikan informasi itu sudah berubah dengan menjalankan perintah `git config --list --local`.
3. Buka akun [Github](https://github.com/) yang akan digunakan, dan buat repositori baru dengan nama yang diinginkan (Contoh yang saya gunakan adalah `goodang_project`). Atur visibilitas menjadi *Public* dan biarkan yang lainnya sesuai *default* nya.
4. Pilih direktori lokal yang sudah diinisiasi Git, di terminal atau *command prompt* jalankan perintah `git branch -M main` untuk membuat branch utama dengan nama "main".
5. Jalankan perintah `git remote add origin <URL_REPO>` untuk menghubungkan direktori lokal dengan repositori di Github. (Gannti URL_REPO dengan URL HTTPS di direktori Github yang sudah dibuat).
6. Buat berkas `.gitignore` di direktori lokal dan diisi dengan teks berikut. (Berkas ini berfungsi untuk mengabaikan beberapa berkas oleh Git)
```.gitignore
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```
7. Untuk melakukan penyimpanan pembaruan dapat melakukan `add`, `commit`, dan `push` dari terminal atau *command prompt* yang dibuka dari direktori lokal.

## **Membuat akun dan *Deploy* di Adaptable.io**
1. Buat akun [Adaptable.io](https://adaptable.io/) menggunakan akun Github yang digunakan untuk membuat proyek.
2. Tekan tombol `New App` dan pilih `Connect an Existing Repository`.
3. Hubungkan Adaptable.io dengan Github dengan memilih `All Repository` pada saat instalasi dan pilih repositori proyek (disini saya menggunakan proyek `goodang_project`) sebagai basisnya. Pilih *branch* yang ingin dijadikan *deployment branch*
4. Pilihlah `Python App Template` sebagai *template* dan `PostgreSQL` sebagai basis data.
5. Sesuaikan versi Python dengan punyamu dan pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn <NAMA_PROYEK>.wsgi`.
6. Masukkan nama aplikasi yang akan jadi nama *domain* situs webmu.
7. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai *Deployment*

## **Bagan *request* dan *response client* dengan Django**
![bagan_request_and_response_client](https://github.com/syauqiarman/goodang_project/assets/113775175/73017ae4-0758-4186-99dc-b888398592dc)


* *User* mengakses website dan melakukan *HTTP request*.
* *Request* yang masuk akan diterima `urls.py` dan akan melakukan proses pencarian terhadap *pattern* url yang sesuai.
* Setelah menemukan yang sesuai, Django akan memanggil fungsi yang sesuai pada `views.py`, disini akan dilakukan *logic handling* dimana database dapat diakses dan diproses yang diambil dari `models.py`.
* `models.py` berfungsi sebagai file yang membuat dan mengatur data yang akan disimpan di database.
* *Database* adalah tempat dimana data aplikasi disimpan, dimana data disini dapat diubah sengan perintah dari `models.py`.
* *Template* disini berfungsi untuk mengatur tampilan halaman web yang akan dikembalikan ke *user*. Setelahnya maka akan dikembalikan ke user dalam bentuk *HTTP response (HTML)*.

## **Mengapa menggunakan *virtual environment*? Bagaimana jika tidak menggunakannya?**
Dengan menggunakan *virtual environment* maka sistem dapat bekerja di ruang yang terisolasi agar proyek yang kita kerjakan tidak berkonflik dengan proyek lain, karena setiap proyek memiliki kebutuhan atau dependensi yang berbeda. Dengan mengaktifkan *virtual environment* maka akan terdapat pembatas atau sekat yang dapat mencegah konflik tersebut.

Meskipun kita bisa membuat aplikasi web Django tanpa mengaktifkan virtual environment, namun sangat tidak disarankan karena kemungkinan besar akan menghadapi konflik antar dependensi dan menjadi sulit untuk mengelola proyek yang sedang dikerjakan. Oleh karenanya disarankan untuk mengaktifkan virtual environment untuk menghindari hal-hal tersebut.

## **MVC, MVT, dan MVVM**
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) merupakan kerangka kerja arsitektur yang digunakan aplikasi dalam proses pengembangannya dengan memisahkan komponen-komponen dan dapat membuat pengelolaa menjadi lebih terstruktur.

## **MVC (Model-View-Controller)**
MVC merupakan kerangka yang membagi aplikasi menjadi 3 bagian, yaitu:
| **Model** | **View** | **Controller** |
| --- | --- | --- |
| Mengatur dan mengelola data aplikasi. | Mengurus logika tampilan informasi yang diambil dari Model kepada pengguna. | Menghubungkan Model dan View, mengatur alur kontrol aplikasi, dan mengolah input dari pengguna. |

## **MVT (Model-View-Template)**
MVT merupakan kerangka yang membagi 3 bagian dan mirip dengan MVC hanya saja controller diganti dengan template. MVT biasa digunakan pada pengembangan web dengan Django.
| **Model** | **View** | **Template** |
| --- | --- | --- |
| Mengatur dan mengelola data aplikasi. | Mengurus logika tampilan informasi yang diambil dari Model kepada pengguna. | Bertanggung jawab untuk merender tampilan dan mengatur bagaimana data dari Model ditampilkan di dalamnya. |

## **MVVM (Model-View-ViewModel)**
MVVM merupakan kerangka yang juga membagi 3 bagian dimana biasa digunakan untukpengembangan aplikasi desktop dan mobile.
| **Model** | **View** | **ViewModel** |
| --- | --- | --- |
| Mengatur dan mengelola data aplikasi. | Menampilkan informasi kepada pengguna berupa tampilan. | Bertindak sebagai perantara antara Model dan View. Ini mengelola logika tampilan dan transformasi data sebelum ditampilkan di View. |

## **Perbedaan Utama MVC, MVT, dan MVVM**
Perbedaan yang utama dari ketiganya dapat dilihat dari bagaimana pengelolaan komunikasi antara Model dan View dilakukan.

* Dalam MVC, Controller memiliki peran yang sangat penting yakni untuk mengatur informasi dari Model dan View.
* Dalam MVT, Template bekerja untuk mengatur tampilan yang akan ada pada web.
* Dalam MVVM, ViewModel bertindak sebagai penghubung dan berusaha untuk mengecilkan ketergantungan antara Model dan View. MVMM juga menerapkan konsep pengikatan data agar ketika ada pembaruan, maka akan otomatis diperbarui tampilannya.
<br/>
<br/>

# **Tugas 3 - Implementasi Form dan Data Delivery pada Django**
Mengimplementasikan Form dan Data Delivery pada Django dan menerapkan beberapa konsep yang telah dipelajari di kelas serta menjawab beberapa pertanyaan.

1. Apa perbedaan antara form POST dan form GET dalam Django?
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

## **Perbedaan form POST dan form GET dalam Django**
Dalam Django metode POST dan GET dapat digunakan untuk mengirim data dari formulir HTML ke server. Berikut adalah perbedaan utama antara keduanya:

1. Metode Pengiriman Data
    | **POST** | **Dalam metode POST, data formulir dikirimkan sebagai bagian dari badan permintaan HTTP. Data ini tidak terlihat dalam URL, yang berarti data sensitif seperti kata sandi lebih aman karena tidak terlihat di baris alamat *browser*.** |
    | --- | --- |
    | **GET** | **Dalam metode GET, data formulir disertakan dalam URL. Data ini terlihat di URL dan dapat dengan mudah dilihat oleh siapa pun dan disimpan dalam riwayat peramban.** |

2. Batas Ukuran Data
    | **POST** | **Metode POST tidak memiliki batasan ukuran data yang ketat, sehingga lebih cocok untuk mengirimkan data besar seperti *file* gambar atau video.** |
    | --- | --- |
    | **GET** | **Metode GET memiliki batasan ukuran data yang lebih kecil karena data harus dimasukkan ke dalam URL. Ini membuatnya kurang cocok untuk mengirim data besar.** |
    
3. Keamanan
    | **POST** | **Metode POST lebih aman untuk mengirim data sensitif karena data tidak terlihat di URL. Ini membuatnya lebih cocok untuk operasi seperti *login* dan pengiriman data pribadi.** |
    | --- | --- |
    | **GET** | **Metode GET kurang aman untuk data sensitif karena data terlihat di URL. Data dapat dengan mudah terlihat oleh orang lain jika ada akses fisik atau jika ada *logging* di server atau perantara.** |  

4. Caching
    | **POST** | **Permintaan POST biasanya tidak akan disimpan dalam cache peramban atau server *proxy* karena operasi POST dianggap tidak idempoten (mengubah data pada server).** |
    | --- | --- |
    | **GET** | **Permintaan GET lebih mungkin akan disimpan dalam cache peramban atau server *proxy* karena operasi GET dianggap idempoten (tidak mengubah data pada server). Ini dapat mempengaruhi kinerja dan privasi data.** | 

Meskipun memiliki beberapa perbedaan, terkadang kita bisa saja membutuhkan keduanya untuk dikombinasikan dalam satu formulir.

## **Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data**
* XML adalah format yang digunakan untuk menyusun data secara hierarkis dan direpresentasikan dengan bentuk *tag* dan atribut. XML umumnya digunakan untuk pertukaran data antar aplikasi, konfigurasi, dan penyimpanan data yang terstruktur. Kelebihan XML adalah fleksibilitasnya yang tinggi dalam mendefinisikan struktur data yang khusus, tetapi kekurangannya adalah ukurannya yang lebih besar dan sintaksis yang cenderung lebih kompleks.
* JSON adalah format data ringkas yang digunakan untuk pertukaran data antar aplikasi dan menggunakan pasangan *key-value* untuk menyimpan data dalam objek. JSON lebih sederhana dan lebih ringkas daripada XML, sehingga lebih mudah dibaca komputer dan manusia. JSON umum digunakan dalam pengembangan *web*, terutama dalam pembangunan *RESTful APIs*.
* HTML digunakan untuk membuat halaman *web* dengan mendefinisikan struktur dan tampilan konten, seperti teks, gambar, tautan, dan elemen interaktif lainnya. Tujuan utamanya adalah mengatur tampilan dan interaksi antarmuka pengguna dalam *browser web*. Pada HTML *tag* sudah ditentukan sehingga tidak bisa untuk membuat *tag* mereka sendiri seperti pada XML dan JSON dalam menyimpan datanya.

## **Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
* JSON menggunakan format yang sederhana dan mudah dipahami oleh manusia. Penggunaan *key-value* dapat dengan mudah diuraikan.
* JSON memiliki format data yang ringan dan memiliki *overhead* yang minimal dalam bentuk karakter tambahan, sehingga meminimalkan penggunaan *bandwidth* saat mentransmisikan data.
* JSON sangat fleksibel untuk melakukan pertukaran data antara berbagai komponen dalam ekosistem aplikasi modern yang sering terdiri dari berbagai teknologi dan bahasa.
* JSON mendukung struktur data yang terintegrasi, yang memungkinkan Anda untuk mewakili data yang kompleks dengan mudah.
* JSON kompatibel dengan JavaScript, sehingga memudahkan pemrosesan dan manipulasi data JSON di sisi klien.
* Umum digunakan dalam implementasi *RESTful APIs* yang populer dalam pengembangan *web* modern. Data JSON dapat dengan mudah diserialisasi dan diterima oleh server dan klien, memfasilitasi interaksi antara keduanya.

## **Implementasi Form dan Data Delivery pada Django**

1. Atur terlebih dahulu routing dari `main/` ke `/` agar bisa mengakses halaman utama secara langsung.
    * Buka `urls.py` yang ada di folder `goodang` dan modifikasi *path* di `urlpatterns` dari `main/` jadi `''`.
        ```python
            urlpatterns = [
                path('', include('main.urls')),
                path('admin/', admin.site.urls),
            ]
        ```
        
2. Mengimplementasi kerangka *views* dengan *skeleton* untuk memastikan konsistensi dalam desain situs *web* kita serta memperkecil kemungkinan terjadinya redundansi kode.
    * membuat folder `templates` pada *root folder* dan buatlah `base.html` di dalamnya sebagai template dasar yang digunakan sebagai kerangka umum untuk halaman *web* lainnya dalam proyek.
        ```html
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta
                    name="viewport"
                    content="width=device-width, initial-scale=1.0"
                />
                {% block meta %}
                {% endblock meta %}
            </head>

            <body>
                {% block content %}
                {% endblock content %}
            </body>
        </html>
        ```

    * Buka `settings.py` pada subdirektori `goodang` dan modifikasi kode pada baris `TEMPLATES`, untuk mendeteksi `base.html` sebagai *template*.
        ```python
        ...
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR / 'templates'],
                'APP_DIRS': True,
                ...
            }
        ]
        ...
        ```
    * Ubah berkas `main.html` pada subdirektori `templates` pada direktori `main` menjadi seperti berikut.
        ```html
        {% extends 'base.html' %}

        {% block content %}
            <h1>Shopping List Page</h1>

            <h5>Name:</h5>
            <p>{{name}}</p>

            <h5>Class:</h5>
            <p>{{class}}</p>
        {% endblock content %}
        ```

3. Membuat form input data dan menampilkan data *item* pada HTML
    * Buat berkas baru dengan nama `forms.py` pada direktori `main` agar bisa menerima data *item* baru. isilah `forms.py` dengan kode berikut.
        ```python
        from django.forms import ModelForm
        from main.models import Item

        class ItemForm(ModelForm):
            class Meta:
                model = Item
                fields = ["owner", "item_name", "category", "amount", "price", "description"]
        ```
    * Pada folder `main`, buka berkas `views.py` dan tambahkan beberapa *import*, lalu buat fungsi baru dengan nama `create_item` dengan parameter `request` agar formulir dapat menambahkan data item secara otomatis setelah di *submit*.
        ```python
        ...
        from django.http import HttpResponseRedirect
        from main.forms import ItemForm
        from django.urls import reverse
        from main.models import Item

        ...

        def create_item(request):
            form = ItemForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return HttpResponseRedirect(reverse('main:show_main'))

            context = {'form': form}
            return render(request, "create_item.html", context)
        ```
    * Modifikasi fungsi `show_main` yang ada pada `views.py` menjadi seperti berikut.
        ```python
        def show_main(request):
            items = Item.objects.all()

            context = {
                'name': 'Syauqi Armanaya Syaki', # Nama kamu
                'class': 'PBP D', # Kelas PBP kamu
                'items': items
            }

            return render(request, "main.html", context)
        ```
    * Buka `urls.py` pada folder `main` lalu *import* fungsi `create_item` yang sudah dibuat.
        ```python
        from main.views import show_main, create_item
        ```
    * Tambahkan *path url* ke dalam `urlpatterns` di `main/urls.py` untuk mengakses fungsi yang sudah di *import*.
        ```python
        path('create-item', create_item, name='create_item'),
        ```
    * Pada direktori `main/templates` buat berkas baru dengan nama `create_item.html` dan isi dengan kode berikut.'
        ```html
        {% extends 'base.html' %} 

        {% block content %}
        <h1>Add New Item</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Add Item"/>
                    </td>
                </tr>
            </table>
        </form>

        {% endblock %}
        ```
    * Buka `main.html` lalu tambahkan kode berikut dalam bagian `{% block content %}` agar data item dapat dilihat dalam bentuk tabel dan tombol "Add New Item" mulai ditampilkan.
        ```html
        <table>
            <tr>
                <th>Owner</th>
                <th>Item Name</th>
                <th>Category</th>
                <th>Amount</th>
                <th>Price</th>
                <th>Description</th>
                <th>Date Added</th>
            </tr>

            {% comment %} Berikut cara memperlihatkan data item di bawah baris ini {% endcomment %}

            {% for item in items %}
                <tr>
                    <td>{{item.owner}}</td>
                    <td>{{item.item_name}}</td>
                    <td>{{item.category}}</td>
                    <td>{{item.amount}}</td>
                    <td>{{item.price}}</td>
                    <td>{{item.description}}</td>
                    <td>{{item.date_added}}</td>
                </tr>
            {% endfor %}
        </table>

        <br />

        <a href="{% url 'main:create_item' %}">
            <button>
                Add New Item
            </button>
        </a>

        {% endblock content %}
        ```
## **Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.**

1. Ubah fungsi `show_main` pada `main/views.py` untuk melihat informasi yang tertera dari hasil *render* HTML.
    ```python
    def show_main(request):
        items = Item.objects.all()

        context = {
            'name': 'Syauqi Armanaya Syaki', # Nama kamu
            'class': 'PBP D', # Kelas PBP kamu
            'items': items
        }

        return render(request, "main.html", context)
    ```
2. Buka `views.py` pada direktori `main` lalu tambahkan *import* `HttpResponse` dan `serializer` seperti berikut.
    ```python
    from django.http import HttpResponse
    from django.core import serializers
    ```
3. Buat fungsi dengan nama `shows_xml` di `views.py` yang menerima parameter *request* untuk mengembalikan data dalam bentuk XML dengan kode berikut.
    ```python
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
4. Buat fungsi dengan nama `shows_json` di `views.py` yang menerima parameter *request* untuk mengembalikan data dalam bentuk JSON dengan kode berikut.
    ```python
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
5. Buat fungsi dengan nama `shows_xml_by_id` di `views.py` yang menerima parameter *request* dan *id* untuk mengembalikan data ID tertentu dalam bentuk XML dengan kode berikut.
    ```python
    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
6. Buat fungsi dengan nama `shows_json_by_id` di `views.py` yang menerima parameter *request* dan *id* untuk mengembalikan data ID tertentu dalam bentuk JSON dengan kode berikut.
    ```python
    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

## **Pembuatan routing URL untuk masing-masing `views` dari yang sudah ditambahkan sebelumnya**
Pada direktori `main`, buka berkas `urls.py` dan *import* fungsi yang sudah dibuat. Kemudian modifikasi *path url* yang ada di dalam `urlpatterns` agar semua fungsi bisa diakses.

```python
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## **Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini"**
Buka `main.html` pada direktori `main/templates`, lalu tambahkan kode yang mengambil *length* dari `items` seperti berikut tepat diatas tabel yang dibuat seperti berikut.
```html
...
<h5>Class:</h5>
    <p>{{class}}</p>
    
    <p>Total of Items: {{items|length}}</p>
    <table>
        <tr>
            <th>Owner</th>
            <th>Item Name</th>
            ...
```

## **Pengaksesan kelima URL di poin 2 menggunakan Postman**
1. Jalankan *virtual environment* terlebih dahulu. Untuk Windows jalankan `env\Scripts\activate.bat` dan untuk Unix(Mac/Linux) jalankan `source env/bin/activate`.
2. Jalankan server dengan perintah `python manage.py runserver`.
3. Buka Postman dan buat *request* baru dengan method `GET`, lalu isi dengan *url* berikut.
   * HTML (http://localhost:8000)
     ![image](https://github.com/syauqiarman/goodang_project/assets/113775175/2fb72eb3-5fa2-4e83-925c-dc8a40967eac)
   * XML (http://localhost:8000/xml)
     ![image](https://github.com/syauqiarman/goodang_project/assets/113775175/1e3f1a0f-116c-4c69-8e91-4f1f04fa775f)
   * JSON (http://localhost:8000/json)
     ![image](https://github.com/syauqiarman/goodang_project/assets/113775175/c79eecef-eb87-4fc1-9e9c-9b8aa711b762)
   * XML by ID (http://localhost:8000/xml/[id])
     ![image](https://github.com/syauqiarman/goodang_project/assets/113775175/998b326b-50ad-4c3a-8356-3862ee864b9d)
   * JSON by ID (http://localhost:8000/json/[id])
     ![image](https://github.com/syauqiarman/goodang_project/assets/113775175/37528e34-9ceb-4b76-9753-78f052050a4c)



