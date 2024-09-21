from django.db import models


class Booth(models.Model):
    name = models.CharField(verbose_name='부스명', max_length=50)
    host = models.CharField(verbose_name='운영주체', max_length=50)
    place = models.CharField(verbose_name='위치', max_length=50)

    DATES = [ 
        ('day1', 'day1'),
        ('day2', 'day2'),
        ('both', 'both'),
    ]
    date = models.CharField(verbose_name='날짜', max_length=10, choices=DATES)
    time_day1 = models.CharField(verbose_name='10/1 운영시간', max_length=20, blank=True, null=True)
    time_day2 = models.CharField(verbose_name='10/2 운영시간', max_length=20, blank=True, null=True)

    CATEGORIES = [
        ('체험', '체험'),
        ('주점', '주점'),
        ('마켓', '마켓'),
    ]
    category = models.CharField(verbose_name='카테고리', max_length=10, choices=CATEGORIES)

    introduction = models.CharField(verbose_name='부스소개', max_length=300, blank=True, null=True)
    image = models.ImageField(verbose_name='사진', upload_to='booth-image', blank=True, null=True)

    def __str__(self):
        return self.name


class MenuGroup(models.Model):
    name = models.CharField(verbose_name='메뉴그룹명', max_length=50)
    price = models.PositiveIntegerField(verbose_name='가격', blank=True, null=True)
    booth = models.ForeignKey(Booth, related_name='menu_group', on_delete=models.CASCADE, verbose_name='해당 부스')

    def __str__(self):
        return f'{self.booth.name} > {self.name}'
    
class Food(models.Model):
    name = models.CharField(verbose_name='음식명', max_length=50)
    price = models.PositiveIntegerField(verbose_name='가격', blank=True, null=True)
    menu_group = models.ForeignKey(MenuGroup, related_name='inner_food', on_delete=models.CASCADE, verbose_name='해당 메뉴그룹')

    def __str__(self):
        return f'{self.menu_group.booth.name} > {self.menu_group.name} > {self.name}'