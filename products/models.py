from django.db import models
import random 
import os


def get_filename_ext(filepath):
  base_name = os.path.basename(filepath)
  name, ext = os.path.splitext(base_name)
  return name, ext

def upload_file(instance,filename):
  print(instance)
  print(filename)
  new_filename = random.randint(0,12345)
  name, ext = get_filename_ext(filename)
  final_filename = '{new_filename}{ext}'.format(new_filename = new_filename, ext = ext)
  return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename,final_filename = final_filename)

class ProductQuerySet(models.query.QuerySet):
  def featured(self):
    return self.filter(featured = True, active = True)

  def active(self):
    return self.filter(active = True)

class ProductManager(models.Manager):

  def get_queryset(self):
    return ProductQuerySet(self.model, using = self._db)

  def all(self):
    return self.get_queryset().active()

  def featured(self): #Product.objects.featured()
    return self.get_queryset().featured()

  def get_by_id(self, id):
    qs = self.get_queryset().filter(id = id)
    if qs.count() == 1:
      return qs.first()
    return None 


# Create your models here.
class Product(models.Model):
  title       = models.CharField(max_length = 120)
  slug        = models.SlugField(blank = True, unique = True)
  description = models.TextField()
  price       = models.DecimalField(decimal_places = 2, max_digits = 10, default = 39.99)
  image       = models.ImageField(upload_to = upload_file, null = True, blank = True )
  featured    = models.BooleanField(default = False)
  active      = models.BooleanField(default = True)

  objects     = ProductManager()

  def get_absolute_url(self):
    return "/products/{slug}/".format(slug = self.slug)

  def __str__(self):
    return self.title
