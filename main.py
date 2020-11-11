import config
import sys

file = "config.yml"
for arg in sys.argv:
    if arg.endswith(".yml"):
        file = arg

config = config.get_info(file)

import course_handler
from datetime import datetime
from models.course import Course
import notifier
import time

if __name__ == "__main__":
    number = config['number']

    print(f"STARTING TRACKING USING TARGET EMAIL: {config['target']}")

    def main():
        notified = False
        watched_courses = list()

        for course in config['courses']:
           watched_courses.append(Course(course, '', '', (0, 0, 0, 0, 0, 0)))
           course_handler.update_class_info(watched_courses[-1])

        for course in watched_courses:
            course.seats = course_handler.get_seat_counts(course)
            print(f'[{datetime.now().strftime("%X")}] {course} is now being tracked!')
            notifier.send_email(f'{course} is now being tracked!')
            notifier.send_sms(f'{course} is now being tracked!')


        while True:
            for course in watched_courses:
                print(f'[{datetime.now().strftime("%X")}] Now checking course: {course}')
                new_seats = course_handler.get_seat_counts(course)

                if new_seats == (-1, -1, -1, -1, -1, -1):
                    print(f'[{datetime.now().strftime("%X")}] Error checking course')
                    if (not notified):
                        notifier.send_email(f'ERROR CHECKING {course}!')
                        notifier.send_sms(f'ERROR CHECKING {course}!')

                        notified = True
                    continue
                notified = False

                if new_seats != course.seats:
                    print(f'[{datetime.now().strftime("%X")}] Seats have changed! {course.seats} -> {new_seats}')

                    course.seats = new_seats

                    if int(new_seats[3]) > 0:
                        notifier.send_email(f'{course} now has a waitlist seat!')
                        notifier.send_sms(f'{course} now has a waitlist seat!')

                    if int(new_seats[0]) > 0:
                        notifier.send_email(f'{course} now has seats!')
                        notifier.send_sms(f'{course} now has seats!')

                    

            time.sleep(3)

    if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            print('\nQuitting from keyboard stop')
            quit()
        except:
            notifier.send_email('PROGRAM CRASHED!')
            notifier.send_sms('PROGRAM CRASHED!')

            main()
