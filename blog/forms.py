# -*- coding: utf-8 -*-
from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text', 'wallpaper')
		labels = {
						'title': 'عنوان المقال',
						'text': 'محتوى المقال',
						'wallpaper': 'صورة العرض'
		}
		

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

"""
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
)
"""
"""
class PostForm(forms.Form):
	title = forms.CharField(label='عنوان المقال')
	text	= forms.CharField(label='محتوى المقال', widget=forms.Textarea)
	wallpaper = forms.FileField(label='صورة العرض', required=False)
"""
