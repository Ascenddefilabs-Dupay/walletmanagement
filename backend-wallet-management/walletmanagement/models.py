# # from django.db import models
# # from django.contrib.auth.hashers import make_password

# # class UserPassword(models.Model):
# #     password = models.CharField(max_length=128)

# #     def save(self, *args, **kwargs):
# #         # self.password = make_password(self.password)
# #         super().save(*args, **kwargs)

# # class RecoveryPhrase(models.Model):
# #     phrase = models.TextField()
# #     created_at = models.DateTimeField(auto_now_add=True)

# from django.db import models
# from django.utils import timezone

# class CryptoWallet(models.Model):
#     wallet_id = models.CharField(max_length=8, unique=True)
#     phrase = models.TextField()  # Correct field name
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)

#     def save(self, *args, **kwargs):
#         if not self.wallet_id:
#             last_wallet = CryptoWallet.objects.all().order_by('wallet_id').last()
#             if last_wallet:
#                 last_id = int(last_wallet.wallet_id[3:])
#                 self.wallet_id = f"DUP{last_id + 1:04d}"
#             else:
#                 self.wallet_id = "DUP0001"
#         super(CryptoWallet, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.wallet_id

# models.py
# models.py
# models.py
from django.db import models
import hashlib

class WalletData(models.Model):
    wallet_id = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=128)
    recovery_phrases = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'crypto_wallet_table'

    def save(self, *args, **kwargs):
        # Hash password
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        
        # Hash recovery phrases
        self.recovery_phrases = hashlib.sha256(self.recovery_phrases.encode()).hexdigest()
        
        # Call the original save method
        super(WalletData, self).save(*args, **kwargs)


    def __str__(self):
        return self.wallet_id


