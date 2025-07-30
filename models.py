from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = (
        ('user', 'Regular User'),
        ('admin', 'Administrator'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')
    is_seller = models.BooleanField(default=False)
    seller_verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


    def can_sell(self):
        return self.is_seller and self.seller_verified



class GemstoneType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Gemstone(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gemstones')
    name = models.CharField(max_length=100)
    description = models.TextField()
    gemstone_type = models.ForeignKey(GemstoneType, on_delete=models.SET_NULL, null=True)
    carat = models.DecimalField(max_digits=5, decimal_places=2)
    CLARITY_CHOICES = [
        ('FL', 'Flawless'),
        ('IF', 'Internally Flawless'),
        ('VVS1', 'Very Very Slightly Included 1'),
        ('VVS2', 'Very Very Slightly Included 2'),
        ('VS1', 'Very Slightly Included 1'),
        ('VS2', 'Very Slightly Included 2'),
        ('SI1', 'Slightly Included 1'),
        ('SI2', 'Slightly Included 2'),
        ('I1', 'Included 1'),
        ('I2', 'Included 2'),
        ('I3', 'Included 3'),
    ]
    clarity = models.CharField(max_length=10, choices=CLARITY_CHOICES)
    certification = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_id = models.CharField(max_length=100, blank=True, null=True)
    certificate_issuer = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='gemstone_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.gemstone_type})"


from django.utils import timezone


class AuctionLot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    gemstones = models.ManyToManyField('Gemstone', related_name='lots')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Auction(models.Model):
    lot = models.OneToOneField(AuctionLot, on_delete=models.CASCADE, related_name='auction')
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    winning_bid = models.OneToOneField('Bid',on_delete=models.SET_NULL,null=True,blank=True,related_name='won_auction')

    @property
    def is_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time and not self.is_closed



class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-amount']




class Payment(models.Model):
    auction = models.OneToOneField(Auction, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ])
    method = models.CharField(max_length=50, choices=[
        ('razorpay', 'Razorpay'),
    ], default='razorpay')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Auction #{self.auction.id} by {self.buyer.username}"


class Report(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    gemstone = models.ForeignKey(Gemstone, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('open', 'Open'),
        ('reviewed', 'Reviewed'),
        ('resolved', 'Resolved'),
    ], default='open')
    created_at = models.DateTimeField(auto_now_add=True)




class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    auction = models.ForeignKey('Auction', on_delete=models.CASCADE, related_name='watched_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'auction')

    def __str__(self):
        return f"{self.user.username} watching Auction #{self.auction.id}"




