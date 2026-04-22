from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Seu nome completo',
                'class': 'w-full bg-white/10 border border-[#C9A227]/40 rounded-lg px-4 py-3 text-white placeholder-white/50 focus:outline-none focus:border-[#C9A227] focus:ring-1 focus:ring-[#C9A227] transition-all duration-200'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Seu melhor e-mail',
                'class': 'w-full bg-white/10 border border-[#C9A227]/40 rounded-lg px-4 py-3 text-white placeholder-white/50 focus:outline-none focus:border-[#C9A227] focus:ring-1 focus:ring-[#C9A227] transition-all duration-200'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Seu telefone (opcional)',
                'class': 'w-full bg-white/10 border border-[#C9A227]/40 rounded-lg px-4 py-3 text-white placeholder-white/50 focus:outline-none focus:border-[#C9A227] focus:ring-1 focus:ring-[#C9A227] transition-all duration-200'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Lead.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email
