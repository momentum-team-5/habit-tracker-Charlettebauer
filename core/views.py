from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit, Record
from .forms import HabitForm, RecordForm


def welcome(request):
    return render(request, "core/welcome.html")


@login_required
def habits_list(request):
    user = request.user
    habits = user.habits.all()
    form = HabitForm()

    return render(request, "core/habits_list.html", {"habits": habits, "form": form})


@login_required
def records_list(request):
    user = request.user
    records = user.records.all()
    form = RecordForm()

    return render(request, "core/records_list.html", {"records": records, "form": form})


@login_required
def habit_details(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    return render(
        request,
        "core/habit_details.html",
        {
            "habit": habit,
        },
    )


@login_required
def habit_add(request):
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("habit_details.html", pk=habit.pk)
    return render(request, "core/habit_add.html", {"form": form})


@login_required
def habit_edit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "GET":
        form = HabitForm(instance=habit)

    else:
        form = HabitForm(instance=habit, data=request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("habit_details", pk=habit.pk)

    return render(request, "habit_edit.html", {"habit": habit, "form": form})


@login_required
def habit_delete(request, habit_pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == "POST":
        habit.delete()
        return redirect("habits_list")

    return render(request, "habit_delete.html", {"habit": habit})


@login_required
def record_add(request, pk, date):
    habit = get_object_or_404(Record, pk=pk)

    if request.method == "GET":
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)

        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.habit = get_object_or_404(Habit, pk=pk)
            if record.number >= habit.number:
                record.is_met = True
            else:
                record.is_met = False
            if habit.is_negative:
                record.is_met = not record.is_met
            record.save()
            return redirect(to="habits_list")
    return render(
        request,
        "core/record_add.html",
        {"form": form, "habit": habit, "date": date, "pk": pk},
    )


@login_required
def record_edit(request, pk):
    record = get_object_or_404(Record, pk=pk)
    habit = record.habit
    if request.method == "GET":
        form = RecordForm(instance=record)
    else:
        form = RecordForm(data=request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            if record.number >= habit.number:
                record.is_met = True
            else:
                record.is_met = False
            if habit.is_negative:
                record.is_met = not record.is_met
            form.save()
            return redirect(to="habits_list")
    return render(
        request,
        "core/record_edit.html",
        {"form": form, "record": record, "habit": habit},
    )
