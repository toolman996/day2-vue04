from django.db import models

# Create your models here.
class MyModel(models.Model):
    sex_chooices = (
        (0, '男'),
        (1, '女'),
    )
    name=models.CharField(max_length=66)
    pwd=models.CharField(max_length=66)
    age=models.CharField(max_length=66)
    sex=models.SmallIntegerField(choices=sex_chooices,default=0)
    img=models.ImageField(upload_to='img',default='img/33.jpg')

    class Meta:
        db_table='tb_manage'
        verbose_name='个人信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name




class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        # 在元数据中可以通过abstract来声明当前表为抽象表  不会在数据库中为当前表生产对应的表结构
        # 其他模型继承这个抽象表后，可以继承表中拥有的字段
        abstract = True


class Book(BaseModel):
    book_name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pic = models.ImageField(upload_to="img", default="img/1.jpg")
    publish = models.ForeignKey(to="Press", on_delete=models.CASCADE,  # 级联删除
                                db_constraint=False,  # 删除后对应的字段可以为空
                                related_name="books", )  # 反向查询的名称
    authors = models.ManyToManyField(to="Author", db_constraint=False, related_name="books")

    class Meta:
        db_table = "tb_book"
        verbose_name = "图书表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name


class Press(BaseModel):
    press_name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to='img', default="img/1.jpg")
    address = models.CharField(max_length=256)

    class Meta:
        db_table = "tb_press"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.press_name


class Author(BaseModel):
    author_name = models.CharField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = "tb_author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author_name


class AuthorDetail(BaseModel):
    phone = models.CharField(max_length=11)
    author = models.OneToOneField(to="Author", on_delete=models.CASCADE, related_name="detail")

    class Meta:
        db_table = "tb_author_detail"
        verbose_name = "作者详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s的详情" % self.author.author_name