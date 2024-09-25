#from django.db import models

# # Create your models here.

# class CryptoWallet(models.Model):
#     wallet_id = models.CharField(max_length=10, unique=True, blank=True)
#     sui_address = models.CharField(max_length=255)
#     balance = models.DecimalField(max_digits=20, decimal_places=2)

#     # class Meta:
#     #     db_table = "crypto_wallet_table"

#     def generate_wallet_id(self):
#         # Fetch the last record and check its custom_id
#         last_account = CryptoWallet.objects.order_by('id').last()

#         if not last_account:
#             # No previous account, starting the sequence
#             return 'DUP0001'
        
#         # Extract number from the last custom_id
#         last_id = last_account.wallet_id
#         id_number = int(last_id.replace('DUP', '')) + 1

#         # Return the new custom_id, padded with zeros
#         return f'DUP{id_number:04d}'

#     def save(self, *args, **kwargs):
#         if not self.wallet_id:
#             self.wallet_id = self.generate_wallet_id()
#         super(CryptoWallet, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.wallet_id
    
    