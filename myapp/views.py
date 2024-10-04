from django.shortcuts import render,redirect


from django.views.generic import View


from myapp.forms import MovieForm

from myapp.models import Movies

from django.contrib import messages

# view=>view for creating new movie
# methods:GET,POST
# url:localhost:8000/movies/add

# Create your views here.

class MovieCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=MovieForm()

        return render(request,"movie_add.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movies.objects.create(

                title=data.get("title"),

                genre=data.get("genre"),

                language=data.get("language"),

                year=data.get("year"),

                run_time=data.get("run_time"),

                director=data.get("director")
            )

            messages.success(request,"Movie has been added")


            return redirect("movie-list")
        
        else:

            messages.error(request,"Failed to add movie")


            return render(request,"movie_add.html",{"form":form_instance})




class MovieListView(View):

    def get(self,request,*args,**kwargs):

        qs=Movies.objects.all()

        return render(request,"movie_list.html",{"movies":qs})
    

# movie detail view
# url:lh:8000/movies/<int:primarykey>/
# url:lh:8000/movies/1/
# url:lh:8000/movies/2/

# method:get



class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id)

        return render(request,"movie_detail.html",{"movie":qs})
    


# movie delete View
# url:lh:8000/movie/<int:pk>/remove/
# method:get


class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Movies.objects.get(id=id).delete()

        messages.success(request,"Movie removed")

        return redirect("movie-list")




class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movies.objects.get(id=id)

        movie_dictionary={

            "title":movie_obj.title,
            "genre":movie_obj.genre,
            "language":movie_obj.language,
            "year":movie_obj.year,
            "run_time":movie_obj.run_time,
            "director":movie_obj.director
        }

        form_instance=MovieForm(initial=movie_dictionary)

        return render(request,"movie_edit.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        id=kwargs.get("pk")

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movies.objects.filter(id=id).update(**data)

            messages.success(request,"Movie has been changed")

            
            return redirect("movie-list")
        
        else:

            messages.error(request,"Movie not changed")

            
            return render(request,"movie_edit.html",{"form":form_instance})