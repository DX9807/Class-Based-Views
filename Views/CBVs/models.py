from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class PostsManager(models.Manager):
    def create_post(self,post_title,post_author):
        post=self.create(post_title=post_title,post_author=post_author)
        return post

def upload_post_image(instance,filename):
    return "media/{post_title}/{filename}/".format(post_title=instance.post_title,filename=filename)



class Posts(models.Model):
    post_title=models.CharField(max_length=300)
    post_image=models.ImageField(upload_to=upload_post_image,blank=True,null=True)
    post_content=models.TextField(blank=True)
    post_date=models.DateTimeField(auto_now_add=True)
    post_author=models.ForeignKey(User,on_delete=models.CASCADE)
    objects=PostsManager()

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("CBVs:detail",kwargs={'pk':self.pk})


    @classmethod
    def create_post(cls,post_title,post_author):
        post=cls(post_title=post_title,post_author=post_author)

        return post
