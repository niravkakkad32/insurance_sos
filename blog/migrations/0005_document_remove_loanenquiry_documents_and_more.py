# Generated by Django 5.0.2 on 2024-02-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_policyissue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.RemoveField(
            model_name='loanenquiry',
            name='documents',
        ),
        migrations.AlterField(
            model_name='loanenquiry',
            name='number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loanenquiry',
            name='rc_book_image',
            field=models.ImageField(upload_to='rc_book_images/'),
        ),
        migrations.AlterField(
            model_name='loanenquiry',
            name='rc_book_radio',
            field=models.CharField(max_length=10),
        ),
        migrations.AddField(
            model_name='loanenquiry',
            name='documents',
            field=models.ManyToManyField(to='blog.document'),
        ),
    ]