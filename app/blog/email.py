from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import reverse

# from user.models import Subscription

class Email:
    def __init__(self, post):
        self.post = post

    def generate_new_post_message(self) -> str:
        html = f"""New post from {self.post.blog.user.username} published at blog 
        <a href='{settings.DOMAIN_NAME}:{settings.PORT}{reverse('blogs:detail', args=[self.post.blog.id])}'>Link</a>
        """
        return html

    def send_new_post_message(self, to: list):
        email_message = EmailMessage("New post", self.generate_new_post_message(),
                                     settings.EMAIL_HOST_USER, to)
        email_message.content_subtype = 'html'
        email_message.send()

    def generate_update_post_message(self) -> str:
        html = f"""Update post from {self.post.blog.user.username} published at link 
                <a href='{settings.DOMAIN_NAME}:{settings.PORT}{reverse('blogs:post', args=[self.post.id])}'>Link</a>
                """
        return html

    def send_update_post_message(self, to: list):
        email_message = EmailMessage("Update post", self.generate_update_post_message(),
                                     settings.EMAIL_HOST_USER, to)
        email_message.content_subtype = 'html'
        email_message.send()
