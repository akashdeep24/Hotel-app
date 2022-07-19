from distutils.command.upload import upload
from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import User




class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4 , editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract= True


class Amenities(BaseModel):
    amenity_name= models.CharField(max_length=200)

    def __str__(self):
        return self.amenity_name
    
class Hotel(BaseModel):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)
    image_one = models.ImageField(upload_to="home/images", default="")
    image_two = models.ImageField(upload_to="home/images", default="")
    image_three = models.ImageField(upload_to="home/images", default="")
    def __str__(self):
        return self.hotel_name

class HotelBooking(BaseModel):
    hotel = models.ForeignKey(Hotel, related_name="hotel_booking", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_booking", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rooms = models.IntegerField(default=0)
    booking_type = models.CharField(max_length=100 ,choices=(('Pre paid', 'Pre paid'),('Post paid', 'Post paid')))
