# Online Library

A simple Python backend-style project for managing a small online library.

## Features

- Add and display users, categories, and books
- Search books by title, author, or category
- Add ratings and reviews from 1 to 10
- Track borrowed and completed books
- Display a user's reading history
- Find books a user has completed
- Recommend books based on highly rated categories
- Calculate average ratings
- Count popular authors and categories with `Counter`
- Save and load data using JSON
- Save and load data using SQLite

## Project files

- `main.py`: Runs the example program
- `models.py`: Defines users, books, categories, ratings, and reading records
- `library.py`: Contains library operations and recommendations
- `storage.py`: Saves and loads JSON data
- `sqlite_storage.py`: Saves and loads SQLite data
- `library_data.json`: JSON data file, created by the program
- `library.db`: SQLite database, created by the program

## Requirements

Python 3.10 or newer. The project uses Python's standard library, so no extra packages are required.

## Run the project

Open a terminal in the project folder and run:

```bash
python main.py


# المكتبة الإلكترونية

مشروع تعليمي بسيط بلغة Python لإدارة مكتبة إلكترونية صغيرة.

## المميزات

- إضافة وعرض المستخدمين والتصنيفات والكتب
- البحث عن الكتب بالعنوان أو المؤلف أو التصنيف
- إضافة تقييمات ومراجعات من 1 إلى 10
- تسجيل استعارة الكتب وإتمام قراءتها
- عرض سجل القراءة الخاص بالمستخدم
- معرفة الكتب التي أكمل المستخدم قراءتها
- اقتراح كتب بناءً على التصنيفات التي حصلت على تقييمات عالية
- حساب متوسط تقييمات الكتب
- إحصاء المؤلفين والتصنيفات الأكثر شيوعًا باستخدام `Counter`
- حفظ البيانات وتحميلها باستخدام JSON
- حفظ البيانات وتحميلها باستخدام SQLite

## ملفات المشروع

- `main.py`: يشغّل البرنامج التجريبي
- `models.py`: يحتوي على كلاسات المستخدمين والكتب والتصنيفات والتقييمات وسجلات القراءة
- `library.py`: يحتوي على وظائف المكتبة والبحث والتوصيات
- `storage.py`: يحفظ البيانات ويحمّلها بصيغة JSON
- `sqlite_storage.py`: يحفظ البيانات ويحمّلها باستخدام SQLite
- `library_data.json`: ملف بيانات JSON، ينشئه البرنامج
- `library.db`: قاعدة بيانات SQLite، ينشئها البرنامج

## المتطلبات

Python إصدار 3.10 أو أحدث. يستخدم المشروع المكتبات المدمجة مع Python، لذلك لا يحتاج إلى تثبيت حزم إضافية.

## تشغيل المشروع

افتح الطرفية داخل مجلد المشروع وشغّل:

```bash
python main.py



يعرض البرنامج أمثلة على وظائف المكتبة. تُنشأ ملفات JSON وSQLite عند تشغيل دوال الحفظ الخاصة بها.
تخزين البيانات
يعرض المشروع طريقتين لتخزين البيانات:
- JSON: يحفظ البيانات في ملف نصي سهل القراءة.
- SQLite: يحفظ البيانات في جداول مترابطة بقيود للمفاتيح الخارجية والقيم.


