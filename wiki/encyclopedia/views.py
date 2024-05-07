from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import util
import markdown2
from django import forms
import random
class Newentry(forms.Form):
    Title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    if util.get_entry(title) != None:
        content = util.get_entry(title)
        content_html = markdown2.markdown(content)
        return render(request, 'encyclopedia/entry_page.html', {
            'entry': title,
            'content': content_html,
        })
    else:
        return render(request, 'encyclopedia/Error.html',
                  {
                      'title': title
                  })

def search(request):
    if request.method == "POST":
        title = request.POST.get('q')  # Retrieve the value of the 'q' input field
        entries = util.list_entries()
        rs = [entry for entry in entries if title in entry]
        if title in entries:
                return entry_page(request,title)

        elif rs :
                 return render(request, "encyclopedia/index.html", 
                {
                    "entries": rs
                })
        else:
            return render(request, 'encyclopedia/Error.html',
                    {
                        'title': title
                    })
def add_entry(request):
    if request.method =='POST':
        form = Newentry(request.POST)
        if form.is_valid():
            title = form.cleaned_data['Title']
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('encyclopedia:entry_page', args=[title]))
    else:

        return render(request,'encyclopedia/add_entry.html',
                   {
                        'form':Newentry()
                   })
    
def edit_entry(request, title):
    if request.method =='POST':
        form = Newentry(request.POST)
        if form.is_valid():
            title = form.cleaned_data['Title']
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('encyclopedia:entry_page', args=[title]))
     
    else: 
            # Retrieve content of the entry with the given title
            entry_content = util.get_entry(title)
            
            # If the entry exists, prepopulate the form fields with its content
            if entry_content:
                initial_data = {'Title': title, 'content': entry_content}
                form = Newentry(initial=initial_data)
            return render(request, 'encyclopedia/edit_entry.html',
                           {
                                'form': form
                            })
def random_page(request):
    all_titles = util.list_entries()
    random_title = random.choice(all_titles)
    return HttpResponseRedirect(reverse('encyclopedia:entry_page', args=[random_title]))