from django.db import models
import hashlib
from django.utils import timezone

class WalletData(models.Model):
    wallet_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=128)
    recovery_phrases = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=10, default='null')
    creation_state = models.CharField(max_length=10, default='null')

    class Meta:
        db_table = 'crypto_wallet_table'

    def save(self, *args, **kwargs):
        # Hash password
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        
        # Hash recovery phrases
        # self.recovery_phrases = hashlib.sha256(self.recovery_phrases.encode()).hexdigest()
        
        # Call the original save method
        super(WalletData, self).save(*args, **kwargs)


    def __str__(self):
        return self.wallet_id

class CustomUser(models.Model):
    user_id = models.CharField(max_length=8, primary_key=True)
    user_email = models.EmailField(unique=True)
    user_first_name = models.CharField(max_length=30)
    user_middle_name = models.CharField(max_length=30, blank=True)
    user_last_name = models.CharField(max_length=30)
    user_dob = models.DateField()
    user_phone_number = models.BigIntegerField()
    user_country = models.CharField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_address_line_1 = models.CharField(max_length=255)  
    user_address_line_2 = models.CharField(max_length=255, blank=True) 
    user_pin_code = models.BigIntegerField()
    user_state = models.CharField(max_length=50)  
    user_profile_photo = models.CharField(max_length=255, blank=True, null=True)
    user_password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50)
    user_old_password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(default=timezone.now, blank=True, null=True)
    registration_status = models.CharField(max_length=10, default='False')

    class Meta:
        db_table = 'users'
        managed= False
