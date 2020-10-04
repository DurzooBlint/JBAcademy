from time import strftime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from datetime import timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

menu_item = None
now = datetime.now().date()
next_week = now + timedelta(days=6)
while menu_item != "0":
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")

    menu_item = input()

    if menu_item == "1":
        tasks = session.query(Task).all()
        print(f"Today {now.strftime('%d')} {now.strftime('%b')}:")
        if not tasks:
            print("Nothing to do!")
        else:
            for task in tasks:
                print(task.task)

    elif menu_item == "2":
        weekday = now
        while weekday <= next_week:
            tasks = session.query(Task).filter(Task.deadline == weekday)
            print(weekday.strftime('%A %d %b:'))
            i = 0
            if tasks.count() == 0:
                print('Nothing to do!')
                print("")
            else:
                for task in tasks:
                    i += 1
                    print(f'{i}. {task.task}')
                print("")
            weekday += timedelta(days=1)

    elif menu_item == "3":
        print("All tasks:")
        tasks = session.query(Task).order_by(Task.deadline).all()
        i = 0
        for task in tasks:
            i += 1
            print(f'{i}. {task.task}. {task.deadline.strftime("%#d %b")}')
        print("")

    elif menu_item == "4":
        print("Missed tasks:")
        tasks = session.query(Task).filter(Task.deadline < now)
        i = 0
        if tasks.count() == 0:
            print('Nothing is missed!')
            print("")
        else:
            for task in tasks:
                i += 1
                print(f'{i}. {task.task}. {task.deadline.strftime("%#d %b")}')
        print("")

    elif menu_item == "5":
        print("Enter task")
        new_task_name = input()
        print("Enter deadline")
        new_task_deadline = datetime.strptime(input(), '%Y-%m-%d')
        new_task = Task(task=new_task_name, deadline=new_task_deadline)
        session.add(new_task)
        session.commit()

    elif menu_item == "6":
        print("Choose the number of the task you want to delete:")
        tasks = session.query(Task).order_by(Task.deadline).all()
        i = 0
        for task in tasks:
            i += 1
            print(f'{i}. {task.task}. {task.deadline.strftime("%#d %b")}')
        option = int(input())
        task_to_del = session.query(Task).filter(Task.id == tasks[option-1].id).delete()
        session.commit()


        print("")

    elif menu_item == "0":
        print("Bye!")
