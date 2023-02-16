from django.http import HttpResponse
from django.shortcuts import render


def pad(n):
    if n <= 9:
        return "0" + str(n)
    return str(n)


def fromHourAndMinutesToTotalMinutes(hour, minutes):
    return hour * 60 + minutes


def fromTotalMinutesToHourAndMinutes(totalminutes):
    return totalminutes // 60, totalminutes % 60


# Create your views here.
def avi(request):
    return HttpResponse("hello")


def schedule(request):
    starthour = 11
    startminutes = 15
    endhours = 17
    endminutes = 35
    duration = 25
    starttotalminutes = fromHourAndMinutesToTotalMinutes(starthour, startminutes)
    endstarttotalminutes = fromHourAndMinutesToTotalMinutes(endhours, endminutes)
    schedules = []
    while starttotalminutes <= endstarttotalminutes:
        shour, sminute = fromTotalMinutesToHourAndMinutes(starttotalminutes)
        newtotalminutes = starttotalminutes + duration
        ehour, eminute = fromTotalMinutesToHourAndMinutes(newtotalminutes)
        schedules.append({"shour": pad(shour), "sminute": pad(sminute), "ehour": pad(ehour), "eminute": pad(eminute)})
        starttotalminutes = newtotalminutes
    return render(request, "schedule.html", {"schedules": schedules})


def hourtomin(request, start, end):
    start = request.GET["start"]
    part1 = start.split(":")
    v1 = int(part1[0])
    m1 = int(part1[1])
    end = request.GET["end"]
    part2 = end.split(":")
    v2 = int(part2[0])
    m2 = int(part2[1])
    v = int(((v2 - v1) * 60 + (m2 - m1)) / 15)
    return v


def mintohour(request, min):
    min = request.GET["min"]
    v1 = (int(min) // 60)
    v2 = (int(min) % 60)
    t = (v1, v2)


def booking(request):
    if request.GET:
        d = hourtomin(request, "start", "end")
        print(d)
    return render(request, "booking.html")


def patientbooking(request):
    if request.GET:
        name= request.GET["name"]
        address= request.GET["add"]
        mobile=request.GET["mobile"]
    return render(request,"patientpage.html")