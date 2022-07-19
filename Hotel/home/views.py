from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import (Amenities , Hotel, HotelBooking)
from django.db.models import Q




def home(request):
    amenities_objs=Amenities.objects.all()
    hotel_objs = Hotel.objects.all()
    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    amenities = request.GET.getlist('amenities')
    if sort_by:
        if sort_by == 'ASC':
            hotel_objs = hotel_objs.order_by('hotel_price')
        elif sort_by == 'DSC':
            hotel_objs = hotel_objs.order_by('-hotel_price')

    if search:
        hotel_objs = hotel_objs.filter(Q(hotel_name__icontains = search)|Q(description__icontains = search))
    
    if len(amenities):
        hotel_objs = hotel_objs.filter(amenities__amenity_name__in = amenities).distinct

    
    context = {'amenities_objs': amenities_objs, 'hotels_objs': hotel_objs, 
    'sort_by':sort_by, 'search':search, 'amenities':amenities,}
    return render(request, 'home/home.html', context)

def check_booking(start_date, end_date, uid, room_count):
        booking_obj = HotelBooking.objects.filter(Q(start_date__lte = start_date, hotel__uid= uid)|Q( 
        end_date__gte= end_date, hotel__uid = uid))
        print(booking_obj)        
        if booking_obj:
            reserved_rooms = booking_obj[0].rooms
            available_rooms = room_count - reserved_rooms
        else: available_rooms = room_count
        print(available_rooms)
        return available_rooms
        


def hotel_detail(request, uid):
    hotel_objs = Hotel.objects.get(uid=uid)
    if request.method == 'POST':
        no_of_rooms= request.POST.get('rooms')
        checkin= request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        hotel = Hotel.objects.get(uid=uid)
        x= check_booking(checkin, checkout, uid, hotel.room_count)
        if x < int(no_of_rooms):
            messages.warning(request, 'Only %s rooms avaialble' %x)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        for i in range(int(no_of_rooms)):
            HotelBooking.objects.create(hotel=hotel, user= request.user, start_date=checkin, end_date=checkout, booking_type= 'Pre Paid', rooms=no_of_rooms)
            messages.warning(request, 'Booked %s rooms' %no_of_rooms)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'hotel_detail.html', {'hotels_obj':hotel_objs})

def login_page(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        user_obj = authenticate(username = username, password = password)
        if not user_obj:
            messages.warning(request, 'Invalid user id or password')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request, user_obj)
        return redirect('/')


    return render(request, 'home/login.html')

def register_page(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            messages.warning(request, 'This email is already registered')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return redirect('/')

    return render(request, 'home/register.html')


