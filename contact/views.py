from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #τωρα απλως εμφανιζουμε ενα μηνυμα επιτυχιας
            messages.success(request, 'Το μήνυμα στάλθηκε με επιτυχία!')
            return redirect('contact_form')
    else:
        form = ContactForm()
        
    return render(request, 'contact/contact_form.html', {'form': form})