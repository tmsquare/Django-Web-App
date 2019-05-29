from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch  import receiver
from django.utils.text import slugify

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status="published")

# Create your models here.

class Post(models.Model):
	objects = models.Manager() #default model manager  
	published = PublishedManager() #our custum model Manager

	STATUS_CHOICES = {
		('draft','Draft'),
		('published','Published'),
	}

	title	=	models.CharField(max_length=100)
	slug	=	models.SlugField(max_length=120)
	author	=	models.ForeignKey(User, related_name='blog_posts', on_delete='CASCADE')
	body	=	models.TextField()
	likes   =   models.ManyToManyField(User, related_name='likes', blank=True)
	created	=	models.DateTimeField(auto_now_add=True)
	updated	=	models.DateTimeField(auto_now=True)   
	status	=	models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
  

	def __str__(self):
		return self.title

	def total_likes(self):
		return self.likes.count()



	def get_absolute_url(self):
		return reverse("blog:post_detail", args=[self.id, self.slug])


@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
	slug = slugify(kwargs['instance'].title)
	kwargs['instance'].slug = slug


class Profile(models.Model):
	objects = models.Manager() #default model manager

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dob = models.DateField(null=True, blank=True)
	photo = models.ImageField(null=True, blank=True)

	def __str__(self):
		return "Profile of user {}".format(self.user.username)


class Images(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/', blank=True, null=True)

	def __str__(self):
		return self.post.title + " Image"

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	reply = models.ForeignKey('Comment', null=True, related_name="replies",on_delete=models.CASCADE)
	content = models.TextField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}-{}'.format(self.post.title, str(self.user.username)) 