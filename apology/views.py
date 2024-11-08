from django.shortcuts import render, redirect
from .models import Response


def apology_view(request):
    return render(request, "apology/apology.html")


def response_view(request):
    if request.method == 'POST':
        response = request.POST.get('response') == 'accept'  # Convert to boolean
        reason = request.POST.get('reason', '')  # Optional field for reason

        # Create the Response object with response and reason
        Response.objects.create(response=response, reason=reason)
        return redirect("thank_you")  # Redirect to a thank-you page

    return render(request, "apology/response.html")


def thank_you_view(request):
    return render(request, 'apology/thank_you.html')