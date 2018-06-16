from django.db import models
from django.conf import settings
import datetime
from django.core.cache import cache
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Holds the User account(s)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    joined = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    # Experimental, though. Will move to NodeJS
    def last_seen(self):
        return cache.get('seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                    seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


# class UserFollowers(models.Model):
#     user = models.OneToOneField(User)
#     date = models.DateTimeField(auto_now_add=True)
#     count = models.IntegerField(default=1)
#     followers = models.ManyToManyField(User, related_name='followers')

#     def __str__(self):
#         return '{}, {}'.format(self.user, self.count)


class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Add following field to User dynamically
User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))
