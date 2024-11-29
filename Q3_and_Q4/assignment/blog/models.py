from django.db import models

#shared schema model

class BlogTenant(models.Model):
    tenant_id = models.CharField(max_length=100, unique=True)  
    blog_name = models.CharField(max_length=200)

    class Meta:
        abstract = True  

class BlogPost(BlogTenant):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.blog_name}"

    class Meta:
        unique_together = ['tenant_id', 'title'] 
