# Generated by Django 4.0.4 on 2022-04-26 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import utils.uploading


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.IntegerField(default=0, verbose_name='общее кол-во товара')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название медианосителя')),
            ],
            options={
                'verbose_name': 'Медианоситель',
                'verbose_name_plural': 'Медианосители',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя музыканта')),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to=utils.uploading.upload_function)),
            ],
            options={
                'verbose_name': 'Музыкант',
                'verbose_name_plural': 'Музыканты',
            },
        ),
        migrations.CreateModel(
            name='MusicGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название жанра')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('is_ready', 'Заказ готов'), ('completed', 'Заказ получен')], default='new', max_length=100, verbose_name='Статус заказа')),
                ('buying_type', models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], max_length=100, verbose_name='Тип заказа')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Дата создания заказа')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата получения заказа')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstore.cart', verbose_name='Корзина')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='musicstore.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('read', models.BooleanField(default=False, verbose_name='Прочтено')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstore.customer')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.CreateModel(
            name='MusicArtist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя исполнителя')),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to=utils.uploading.upload_function)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstore.musicgenre')),
                ('members', models.ManyToManyField(related_name='artist', to='musicstore.member', verbose_name='Участник')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
        migrations.CreateModel(
            name='MusicAlbums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название альбома')),
                ('songs_list', models.TextField(verbose_name='Трэклист')),
                ('release_date', models.DateField(verbose_name='Дата релиза')),
                ('slug', models.SlugField()),
                ('description', models.TextField(default='Описание появится позже', verbose_name='Описание')),
                ('stock', models.IntegerField(default=0, verbose_name='Наличие на сладе')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('offer_of_the_week', models.BooleanField(default=False, verbose_name='Предложение недели')),
                ('image', models.ImageField(upload_to=utils.uploading.upload_function)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstore.musicartist', verbose_name='Исполнитель')),
                ('media_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstore.mediatype', verbose_name='Носитель')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to=utils.uploading.upload_function)),
                ('use_in_slider', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Галерея изображений',
                'verbose_name_plural': 'Галерея изображений',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_orders',
            field=models.ManyToManyField(blank=True, related_name='related_customer', to='musicstore.order', verbose_name='Заказы покупателя'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='customer',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to='musicstore.musicalbums', verbose_name='Список ожидаемого'),
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstore.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstore.customer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Продукт корзины',
                'verbose_name_plural': 'Продукты корзины',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstore.customer', verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_cart', to='musicstore.cartproduct', verbose_name='Продукты для корзины'),
        ),
    ]
