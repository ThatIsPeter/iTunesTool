"""Peter's handy dandy tool for all sorts of lovely iTunes library stats"""

banner_data = """
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
"""
__version__ = '7.0'
__author__ = 'Peter Miedema'
__copyright__ = 'Copyright 2016-2018 Peter Miedema'

from tkinter import *
from tkinter.ttk import *
from time import asctime, time, mktime
from glob import glob
from os import chdir
from copy import deepcopy
from datetime import datetime

TIME_CONSTANT = 3600000  # The number of iTunes ticks in an hour
SECONDS_2000 = 946684800 # Number of seconds between 00:00:00 1/1/1970 and 00:00:00 1/1/2000

class Track(object):
    """Creates the track object"""
    def __init__(self, title, plays, time, year, artist, rating, album_artist, album, added, genre, love, podcast, last_played):
        self.title = title
        self.plays = int(plays)
        self.time = int(time)
        self.year = int(year)
        self.artist = artist
        self.rating = rating
        self.album_artist = album_artist
        self.album = album
        self.added = added
        self.genre = genre
        self.love = love
        self.podcast = podcast
        self.last_played = int(last_played)
        
    def __str__(self):
        return "{} -- '{}'".format(self.artist, self.title)
    
    def art_type(self, entered_type):
        num = entered_type.lower()
        if num == 'artist':
            result = self.artist
        elif num == 'album artist':
            result = self.album_artist
        elif num == 'year':
            result = self.year
        elif num == 'album':
            result = "{} ({})".format(self.album, self.artist)
        elif num == 'track' or num == 'title':
            result = "{} -- '{}'".format(self.artist, self.title)
        elif num == 'plays':
            result = self.plays
        elif num == 'time':
            result = self.time
        elif num == 'rating':
            result = '*'*int(self.rating/20)
        elif num == 'genre':
            result = self.genre
        elif num == 'love':
            if self.love == True:
                result = 'Loved'
            else:
                result = 'Not Loved'
        else:
            result = None
        return result  
    
class Library(object):
    """An object for the library of tracks"""
    def __init__(self, pure_tracks):
        """Initialises object"""
        self.pure_tracks = pure_tracks
        self.tracks = deepcopy(pure_tracks)
        self.sorter = 'artist'
        self.write_state = False
        self.podcasts = False
        self.remove_podcasts()
        self.file = None

    def open_file(self, title='iTunes Data'):
        """Creates a new text file for writing data"""
        name = title + str(asctime()).replace(':', '-') + '.txt'
        self.file = open(name, 'w', encoding="utf8")

    def try_open_file(self, title):
        """Opens a file for writing if write mode enabled"""
        if self.write_state == True:
            self.open_file(title.capitalize())
            print('File opened for writing.\n')
    
    def try_close_file(self):
        """Tries to close the write file. Will raise error when write is false."""
        try:
            self.file.close()
            print('File write successful!\n')
        except AttributeError:
            pass

    def toggle_write_state(self):
        """Handle for GUI window"""
        if self.write_state == True:
            self.write_state = False
            print('Stats will display in console.')
        else:
            self.write_state = True
            print('Stats will write to a dated file.')

    def toggle_podcasts(self):
        """Handle for GUI window"""
        if self.podcasts == True:
            self.podcasts = False
            self.remove_podcasts()
            print('Podcasts will not be included.')
        else:
            self.podcasts = True
            self.reset_tracks()
            print('Podcasts will be include (library has been reset).')

    def remove_podcasts(self):
        """Removes podcasts from a library"""
        purged_tracks = {}
        for track in self.tracks:
            if self.tracks[track].podcast == False:
                purged_tracks[track] = self.tracks[track]
        self.tracks = purged_tracks

    def set_sorter(self, new_sorter):
        """Because GUI window won't allow definition"""
        self.sorter = new_sorter

    def reset_tracks(self):
        """Resets tracks after subtraction"""
        self.tracks = deepcopy(self.pure_tracks)
        print('\nLibrary reset.\n')

    def line(self, a_line):
        """Displays or writes a line to the file, if one is open"""
        if self.write_state == True:
            try:
                self.file.write(a_line + '\n')
            except AttributeError:
                print('Tried to write to a file, but none was open!')
        else:
            print(a_line)

    def print_list(self, dictionary, sorted_list, line_str, header, footnote="\n"):
        """
        Displays data to the console, where each value of sorted_list is printed with
        the respective value from the dictionary. line_str is the string which is
        repeated for every body line. x is the the content of the list (track, artist,
        etc.) expressed as a string. sorting is a string which expresses what x is
        being sorted by (number of plays, average rating etc.).
        """
        self.try_open_file(header)
        self.line("="*80)
        self.line(header.capitalize())
        self.line("="*80+"\n")
        rank = 1
        for entry in sorted_list:
            if type(dictionary[entry]) == list and len(dictionary[entry]) > 1:
                lock = rank
                for subentry in dictionary[entry]:
                    rank += 1
                    try:
                        self.line(line_str.format(str(lock)+'.=', subentry, entry))
                    except UnicodeEncodeError:
                        self.line("(Line has naughty characters that can't be shown)")
            else:
                try:
                    if type(dictionary[entry]) == str:
                        self.line(line_str.format(str(rank)+'. ', dictionary[entry], entry))
                    else:
                        self.line(line_str.format(str(rank)+'. ', dictionary[entry][0], entry))
                except IndexError:
                    self.line(line_str.format(str(rank)+'. ', dictionary[entry], entry))
                except UnicodeEncodeError:
                    self.line("(Line has naughty characters that can't be shown)")
                rank += 1
        self.line(footnote)
        self.line("="*80)
        self.try_close_file()

    def print_artist_average_years(self, averages):
        """Prepares data and either displays it or writes it to file"""
        year_list = []
        flipped_dict = {}
        for artist in averages:
            if averages[artist] in flipped_dict:
                flipped_dict[averages[artist]].append(artist)
            else:
                flipped_dict[averages[artist]] = [artist]
                year_list.append(averages[artist])
        year_list = sorted(year_list, reverse=True)
        self.try_open_file('{} Year Averages '.format(self.sorter.capitalize()))
        self.line('{}s sorted by average release year:\n'.format(self.sorter.capitalize()) + '='*80 + '\n') #Header
        rank = 1
        for year in year_list:
            if len(flipped_dict[year]) > 1:
                lock = rank
                rank -= 1
                for artist in flipped_dict[year]:
                    self.line("{:>4}.= {:<50} [ {:.2f} ]".format(lock, artist, year))
                    rank += 1
            else:
                self.line("{:>4}.  {:<50} [ {:.2f} ]".format(rank, flipped_dict[year][0], year))
            rank += 1
        self.line('(Plus any year-less artists)') #footer
        self.try_close_file()

    def merge_alike_tracks(self):
        """Adds the plays of alike tracks to single track with the ID one"""
        unique_names = {} #(title, artist) key; ID value
        unique_tracks = {}
        for track in self.tracks:
            if (self.tracks[track].title, self.tracks[track].artist) in unique_names:
                track_id = unique_names[(self.tracks[track].title, self.tracks[track].artist)]
                unique_tracks[track_id].plays += self.tracks[track].plays
            else:
                unique_tracks[track] = self.tracks[track]
                unique_names[self.tracks[track].title, self.tracks[track].artist] = track
        self.tracks = unique_tracks
        print('\nMerge alike tracks ON (reset to disable)\n')

    def get_total_plays(self):
        """Returns the sum of all the plays of a library"""
        play_sum = 0
        for track in self.tracks:
            play_sum += self.tracks[track].plays
        return play_sum

    def get_total_time(self):
        """Returns the sum of all the time spent listening to a library (in hours)"""
        time_sum = 0
        most_time = 0
        most_track = None
        for track in self.tracks:
            track_time = self.tracks[track].plays * self.tracks[track].time
            if most_time <= track_time:
                most_time = track_time
                most_track = track
            time_sum += track_time
        time_sum /= TIME_CONSTANT
        return time_sum, most_track

    def average_last_plays(self):
        """Returns a dictionary of sorters with the average date they were last played"""
        sum_dict = {}
        count_dict = {}
        for track in self.tracks:
            key = self.tracks[track].art_type(self.sorter)
            if key in count_dict:
                sum_dict[key] += self.tracks[track].last_played
                count_dict[key] += 1
            else:
                sum_dict[key] = self.tracks[track].last_played
                count_dict[key] = 1
        average_dict = {}
        for key in count_dict:
            average_dict[key] = int(sum_dict[key]/count_dict[key])
        return average_dict

    def get_plays_per_week(self):
        """
        Takes the tracks dictionary and returns a dictionary with plays per day and
        the respctive x for that key, and the unique plays per day.
        """
        ppd_dict = {}
        current = time()
        for track in self.tracks:
            try:
                ppd = self.tracks[track].plays*604800/(current - self.tracks[track].added)
                if self.tracks[track].art_type(self.sorter) in ppd_dict:
                    ppd_dict[self.tracks[track].art_type(self.sorter)][0] += 1
                    ppd_dict[self.tracks[track].art_type(self.sorter)][1] += ppd
                else:
                    ppd_dict[self.tracks[track].art_type(self.sorter)] = [1, ppd]
            except AttributeError:
                break
        return ppd_dict

    def plays_per_week_average(self):
        """Returns the average number of plays per week for an average song in x"""
        ppd_dict = self.get_plays_per_week()
        for title in ppd_dict:
            ppd_dict[title] = ppd_dict[title][1] / ppd_dict[title][0]
        return ppd_dict

    def plays_per_week(self):
        """Returns the average number of plays per week for x"""
        ppd_dict = self.get_plays_per_week()
        for title in ppd_dict:
            ppd_dict[title] = ppd_dict[title][1]
        return ppd_dict
        
    def loves(self):
        """Returns a list of sorters with the respective number of loves"""
        unique_sorts = []
        love_dict = {}
        for track in self.tracks:
            if self.tracks[track].love == True:
                if self.tracks[track].art_type(self.sorter) in unique_sorts:
                    love_dict[self.tracks[track].art_type(self.sorter)] += 1
                else:
                    love_dict[self.tracks[track].art_type(self.sorter)] = 1
                    unique_sorts.append(self.tracks[track].art_type(self.sorter))
        return love_dict

    def love_percentage(self):
        """Returns a list of sorters with their average loves"""
        love_dict = {}
        sort_dict = {}
        for track in self.tracks:
            sort = self.tracks[track].art_type(self.sorter)
            if sort in sort_dict:
                sort_dict[sort] += 1
            else:
                sort_dict[sort] = 1
            if self.tracks[track].love == True:
                if sort in love_dict:
                    love_dict[sort] += 1
                else:
                    love_dict[sort] = 1
        perc_dict = {}
        for item in love_dict:
            perc_dict[item] = 100*love_dict[item]/sort_dict[item]
        return perc_dict

    def print_love_percentage(self):
        """Displays or writes the love percentage for sorter"""
        loves_dict = self.love_percentage() 
        flipped_dict = flip_dict(loves_dict)[0]
        unique_loves = sorted(flipped_dict.keys(), reverse=True)
        line_str = "{:>7} {:<50} ({:.2f}% loved)"
        header = '{} by percentage loved.'.format(self.sorter.capitalize()) 
        self.print_list(flipped_dict, unique_loves, line_str, header)

    def average_release_year(self):
        """Takes the tracks and finds the mean average year it was released"""
        track_sum = 0
        year_sum = 0
        for track_id in self.tracks.keys():
            if self.tracks[track_id].year != 0:
                track_sum += 1
                year_sum += self.tracks[track_id].year
        return year_sum / track_sum

    def times(self, sorter=None):
        """Takes the tracks and returns a dictionary of x and listening time in hours"""
        if sorter == None:
            sorter = self.sorter
        times = {}
        for track_id in self.tracks.keys():
            time = self.tracks[track_id].plays * self.tracks[track_id].time
            artist = self.tracks[track_id].art_type(sorter)
            if artist in times:
                times[artist] += time / TIME_CONSTANT
            else:
                times[artist] = time / TIME_CONSTANT
        return times

    def percent_played(self):
        """Takes the tracks and returns a dictionary of x and percentage played"""
        percentages = {}
        played_dict = self.filter_one_check()
        sum_dict = self.track_sum()
        for artist in sum_dict:
            try:
                percentages[artist] = played_dict[artist]/sum_dict[artist]*100
            except KeyError:
                percentages[artist] = 0
        return percentages

    def average_times(self):
        """Takes the tracks and returns a dictionary of x and average time in minutes"""
        times = {}
        counts = {}
        for track_id in self.tracks.keys():
            time = self.tracks[track_id].time
            artist = self.tracks[track_id].art_type(self.sorter)
            if artist in times:
                times[artist] += time / TIME_CONSTANT
                counts[artist] += 1
            else:
                times[artist] = time / TIME_CONSTANT
                counts[artist] = 1
        averages = {}
        for artist in counts:
            minutes = int(60*times[artist]/counts[artist])
            seconds = str(round(60*(60*times[artist]/counts[artist] - minutes)))
            if len(seconds) == 1:
                seconds = '0' + seconds
            averages[artist] = "{}:{}".format(str(minutes), seconds)
        return averages

    def get_plays(self):
        """Takes the tracks and returns a dictionary of x and number of plays"""
        plays = {}
        for track_id in self.tracks.keys():
            play = self.tracks[track_id].plays
            artist = self.tracks[track_id].art_type(self.sorter)
            if artist in plays:
                plays[artist] += play
            else:
                plays[artist] = play
        return plays
    
    def track_sum(self):
        """Returns a dict of x with the number of tracks"""
        track_dict = {}
        for track_id in self.tracks.keys():
            artist = self.tracks[track_id].art_type(self.sorter)
            if artist in track_dict:
                track_dict[artist] += 1
            else:
                track_dict[artist] = 1
        return track_dict

    def artist_average_year(self):
        """
        Takes a library and artist type indicator, 
        and then returns every the average release year for every artist
        """
        year_sums = {}
        song_counts = {}
        for track_id in self.tracks.keys():
            artist = self.tracks[track_id].art_type(self.sorter)
            year = self.tracks[track_id].year
            if year != 0:
                if artist in year_sums:
                    year_sums[artist] += year
                    song_counts[artist] += 1
                else:
                    year_sums[artist] = year
                    song_counts[artist] = 1
        averages = {}
        for artist in song_counts.keys():
            averages[artist] = year_sums[artist] / song_counts[artist]
        return averages

    def pre_average_rating(self):
        """Computes the unrounded average rating for the tracks for each sorter"""
        sorter_dict = {}
        for track in self.tracks.keys():
            sorter = self.tracks[track].art_type(self.sorter)
            rating = self.tracks[track].rating / 20
            if rating != 0:
                if sorter in sorter_dict.keys():
                    sorter_dict[sorter][0] += rating
                    sorter_dict[sorter][1] += 1
                else:
                    sorter_dict[sorter] = [rating, 1]
        return sorter_dict
                    
    def average_rating(self):
        """Flips the average ratings"""
        sorter_dict = self.pre_average_rating()
        rating_dict = {}
        ratings = []
        for srt in sorter_dict.keys():
            av = sorter_dict[srt][0] / sorter_dict[srt][1]
            if av in rating_dict:
                rating_dict[av].append(srt)
            else:
                rating_dict[av] = [srt]
                ratings.append(av)
        return rating_dict, ratings

    def year_counts(self):
        """Returns a dictionary of each year and the number of tracks"""
        years = {}
        for track_id in self.tracks.keys():
            year = self.tracks[track_id].year
            if year in years:
                years[year] += 1
            else:
                years[year] = 1
        return years

    def print_basics(self):
        """Displays the total plays"""
        time, most_time = self.get_total_time()
        av_year = self.average_release_year()  
        big_time = self.tracks[most_time].plays * self.tracks[most_time].time / TIME_CONSTANT
        top_1_time = self.top_percent_time(1)
        top_10_time = self.top_percent_time(10)
        top_50_time = self.top_percent_time(50)
        self.try_open_file('Time basics ')
        self.line('\nAverage release year: {:.1f}'.format(av_year))  
        self.line('\nTotal plays: ' + str(self.get_total_plays()))
        self.line('Total time (hours): ' + str(round(time, 2)))
        self.line('Total time (days): ' + str(round(time / 24, 2)))
        self.line("Your most played song by time is '" + self.tracks[most_time].title + "' by " + self.tracks[most_time].artist + ".")
        self.line('You have spent {:.2f} hours listening to this song.'.format(big_time))
        self.line('\nThe most listened 1% of songs hold {:.2f}% of all the time spent listening to this library,'.format(top_1_time))
        self.line('the top 10% hold {:.2f}%, and the top 50% hold {:.2f}%.'.format(top_10_time, top_50_time))
        self.try_close_file()

    def top_percent_time(self, percent, x='track'):
        """
        Takes the library and returns the percentage of total time spent listening
        to the top % of most listened songs
        """
        total_time = self.get_total_time()[0]
        time_list = sorted(self.times(x).values(), reverse=True)
        sub_sum = 0
        for i in range(0, round(len(self.tracks)*percent/100)):
            sub_sum += time_list[i]
        return sub_sum*100 / total_time

    def csv_dump(self):
        """Creates csv full of stats"""
        time_d = self.times()
        play_d = self.get_plays()
        ppw_d = self.plays_per_week()
        ppa_d = self.plays_per_week_average()
        ratings = self.pre_average_rating()
        age = self.artist_average_year()
        playedd = self.percent_played()
        track_count = self.track_sum()
        a_times = self.average_times()
        love = self.loves()
        love_p = self.love_percentage()
        
        name = 'iTunes Stats {}.csv'.format(str(asctime()).replace(':', '-'))
        file = open(name, 'w', encoding="utf8")
        file.write("{},Total Plays,Total Time,Average Length,Plays per Week, Average Plays per Week,Average Release Year,Total Stars,% Played,Tracks,Average Rating,Total Loves,% Loved".format(self.sorter.capitalize()))
        for x in time_d:
            try:
                t_love = love[x]
                t_love_p = love_p[x]
            except KeyError:
                t_love = 0
                t_love_p = 0
            try:
                sorr = x.replace(',','-')
                rate_av = ratings[x][0]/ratings[x][1]
                file.write("\n{},{},{},{},{},{},{},{},{},{},{},{},{}".format(sorr,play_d[x],time_d[x],a_times[x],ppw_d[x],ppa_d[x],age[x],ratings[x][0],playedd[x]*100,track_count[x],rate_av,t_love,t_love_p))
            except KeyError:
                pass
        file.close()
        print('CSV complete.')

    def filter_one_check(self, check='plays', exclude=0):
        """
        Takes the tracks and returns a dictionary of sorters with the number of
        tracks where the check attribute does not match the exclude value.
        """
        played_dict = {}
        for track_id in self.tracks.keys():
            if self.tracks[track_id].art_type(check) != exclude:
                artist = self.tracks[track_id].art_type(self.sorter)
                if artist in played_dict:
                    played_dict[artist] += 1
                else:
                    played_dict[artist] = 1
        return played_dict

    def rating_info(self):
        """
        Returns a dictionary of the average rating and
        the quantity of songs with the different ratings
        """
        zeros, ones, twos, threes, fours, fives = 0, 0, 0, 0, 0, 0
        count = 0
        rating_sum = 0
        for track in self.tracks.keys():
            rating = self.tracks[track].rating
            if rating == 20:
                ones += 1
            elif rating == 40:
                twos += 1
            elif rating == 60:
                threes += 1
            elif rating == 80:
                fours += 1
            elif rating == 100:
                fives += 1
            else:
                zeros += 1
                count -= 1
            count += 1
            rating_sum += rating
        info = {}
        info['zero_average'] = rating_sum / len(self.tracks)
        info['no_zero_average'] = rating_sum / count
        info['ones'] = ones
        info['twos'] = twos
        info['threes'] = threes
        info['fours'] = fours
        info['fives'] = fives
        info['zeros'] = zeros
        return info   

    def print_rating_info(self, info):
        """Displays info collected in rating_info"""
        ratings = ['zeros', 'ones', 'twos', 'threes', 'fours', 'fives']
        track_total = 0
        for rating in ratings:
            track_total += info[rating]
        self.try_open_file('Rating info ')
        self.line('\nThe average rating with unrated tracks treated as zero is {:.2f}.'.format(info['zero_average'] / 20))
        self.line('The average rating when unrated tracks are ignored is {:.2f}.\n'.format(info['no_zero_average'] / 20))
        rate_num = 0
        self.line('Rating:   Quantity:   Percentage:\n' + 80*'=')
        for rating in ratings:
            self.line("{:<9} {:<11} {:.2f}%".format(rate_num, info[rating], info[rating] / track_total*100))
            rate_num += 1
        self.try_close_file()

    def unique_tracks(self):
        """
        Takes the dictionary of IDs and returns a dictionary of (artist, song) keys
        with total play count and time as values.
        """
        u_tracks = {}
        for track in self.tracks:
            if (track.artist, track.title) in u_tracks:
                plays = u_tracks[(track.artist, track.title)][0] + track.plays
                time = u_tracks[(track.artist, track.title)][1] + track.plays*track.time
                u_tracks[(track.artist, track.title)] = (plays, time)
            else:
                u_tracks[(track.artist, track.title)] = (track.plays, track.plays*track.time)
        return u_tracks
        
    def print_year_counts2(self, years, years_list):
        """Displays the year counts to the console"""
        self.try_open_file('Year Counts ')
        try:
            self.line('\n{} songs have no year associated with them.'.format(years[0]))
            years_list.remove(0)
        except KeyError:
            self.line('\nAll songs have a year associated with them (nice).')
        self.line('\nNumber of songs for each year present in the library:')
        max_count = 0
        for year in years_list:
            if years[year] > max_count:
                max_count = years[year]
        scale = 67/max_count
        for year in years_list:
            self.line('{} - {:<4} {}'.format(year, years[year], round(scale*years[year])*']'))
        self.try_close_file()

    def find_artists(self, sorter='artist'):
        """Finds all the artists in the library"""
        unique_artists = []
        for track in self.tracks:
            if self.tracks[track].art_type(sorter) not in unique_artists:
                unique_artists.append(self.tracks[track].art_type(sorter))
        return unique_artists

    def print_year_counts(self, years):
        """Presents the year count function for a library"""
        years_list = []
        for year in years.keys():
            years_list.append(year)
        years_list = sorted(years_list, reverse=False)
        self.print_year_counts2(years, years_list)

    def print_average_rating(self, rating_dict, ratings):
        """Displays or writes the average ratings of a label"""
        ratings = sorted(ratings, reverse=True)
        header = '{}s sorted by average rating (unrated tracks ignored)'.format(self.sorter.capitalize())
        footer = '(Plus any unrated {}s)'.format(self.sorter)
        line_style = "{:>5} {:<50} {:.2f} stars"
        self.print_list(rating_dict, ratings, line_style, header, footer)

    def print_plays_per_week_average(self):
        """Displays or writes the average plays per song per average week"""
        ppd = self.plays_per_week_average()
        header = '{} by average plays per average week.'.format(self.sorter.capitalize()) 
        self.prepare_list(ppd, "({:.2f} average plays per week)",header)
        
    def print_plays_per_week(self):
        """Displays or writes the average plays per week"""
        ppd = self.plays_per_week()
        header = '{} by total plays per average week.'.format(self.sorter.capitalize()) 
        self.prepare_list(ppd, "({:.2f} plays per week)",header)

    def print_loves(self):
        """Displays or writes the loves per sorter"""
        loves_dict = self.loves() 
        header = '{} by loves.'.format(self.sorter.capitalize()) 
        self.prepare_list(loves_dict, "({:.2f} loves)",header)

    def print_times(self):
        """Displays or writes a nice ordered list of a label by play time"""
        times = self.times()
        header = '{} by total time.'.format(self.sorter.capitalize())
        footer = '(Plus any unplayed {}s)'.format(self.sorter)    
        self.prepare_list(times, "({:.2f} hours)",header,footer)

    def print_average_last_plays(self):
        """Prints list of average last play dates"""
        dates = self.average_last_plays()
        header = '{} by average last play.'.format(self.sorter.capitalize())
        footer = '(Plus any unplayed {}s)'.format(self.sorter)    
        self.prepare_list(dates, "{:.1f}",header,footer)
    
    def print_percent_played(self):
        """Displays or writes a nice ordered list of a label by play time"""
        percent_played = self.percent_played()
        header = '{} by percent unplayed.'.format(self.sorter.capitalize())
        footer = '(Plus any unplayed {}s)'.format(self.sorter)    
        self.prepare_list(percent_played, "{:.2f} %",header,footer)
        
    def print_average_times(self):
        """Displays or writes a nice ordered list of a label by average length"""
        averages = self.average_times()
        header = '{} by average length.'.format(self.sorter.capitalize())
        footer = '(Plus any unplayed {}s)'.format(self.sorter)    
        self.prepare_list(averages, "[ {} ]",header,footer)
        
    def print_plays(self):
        """Displays or writes a nice ordered list of a label by play time"""
        plays = self.get_plays()
        header = '{} by total plays.'.format(self.sorter.capitalize())
        footer = '(Plus any unplayed {}s)'.format(self.sorter)
        self.prepare_list(plays, "[ {} ]",header,footer)

    def prepare_list(self, dictionary, data_style, header, footer='\n'):
        """Takes a dictionary and prepares it for printing. Makes a sorted list for the list to print in order."""
        flipped_dict = flip_dict(dictionary)[0]
        sorted_list = sorted(flipped_dict.keys(), reverse=True)
        line_str = "{:>7} {:<50}" + data_style
        self.print_list(flipped_dict, sorted_list, line_str, header, footer)

    def subtract_tracks(self, old_file):
        """Returns a modified track dict with the plays of an old dict subtracted"""
        print("{} plays subtracted from library. Reset to reverse.".format(old_file))
        old_tracks = load_file(old_file)
        for track in self.tracks:
            try:
                self.tracks[track].plays -= old_tracks[track].plays
            except KeyError:
                pass

def backup_library():
    """Takes the library file and saves a backup with a timestamp"""
    file = open('iTunes Music Library.xml', 'r' , encoding="utf8")
    backup = open("iTunes Music Library (" + asctime().replace(':','-') + ").xml", 'w', encoding="utf8")
    for line in file:
        backup.write(str(line))
    backup.close()
    file.close()
    print("Backup Successful.")
    
def load_file(file='iTunes Music Library.xml'):
    """Trys to load a given file, otherwise the default iTunes library file"""
    t1 = time()
    load = False
    while load == False:
        try:
            file = open(file, 'r' , encoding="utf8")
            tracks = MakeDictionary().generate(file)
            t2 = time()
            print('\nLibrary loaded successfully in {:.2f} seconds!'.format(t2-t1))
            file.close()
            load = True
            return tracks
        except FileNotFoundError:
            print('\nThe iTunes library could not be found! Is it in the directory of this program?')
            input('Press enter to try again.')
        except LookupError:
            print('Problem opening the file, possible trouble with encoding!')
            input('Press enter to try again.')
        
def find_libs():
    """Finds all the itunes libraries in the directory"""
    files = []
    for file in glob("*.xml"):
        files.append(file)
    return files

#def filter_artist(artist, sorter='artist'):
    #"""Boils the library down to one artist"""
    #global tracks

def flip_dict(dictionary):
    """
    Takes a dictionary of times and flips the keys and values and a list of 
    all value keys sorted largest to smallest
    """
    sorted_list = []
    flipped_dict = {}
    for key in dictionary:
        if dictionary[key] in flipped_dict:
            flipped_dict[dictionary[key]].append(key)
        else:
            flipped_dict[dictionary[key]] = [key]
            sorted_list.append(key)
    sorted_list = sorted(sorted_list, reverse=True)
    return flipped_dict, sorted_list

def date(unix):
    """Returns a unix time as a readable date and time"""
    return datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')

def gui_window(it_lib):
    """Creates a tkinter window"""
    window = Tk()
    window.wm_title("iTunes Tool 7")
    window.resizable(0, 0)
    try:
        window.iconbitmap('itunestoolicon.ico')
    except TclError:
        print("\nCouldn't load the icon... but that's okay.\n")
    
    banner = PhotoImage(data=banner_data)
    label1 = Label(image=banner)
    label1.grid(row=0, column=0, columnspan=3, pady=10, padx=15, sticky=W)
    
    label_general = Label(window, text="General:", font=("Arial Bold", 12))
    label_sortable = Label(window, text="Sortable Lists:", font=("Arial Bold", 12))
    label_settings = Label(window, text="Settings:", font=("Arial Bold", 12))
    label_general.grid(row=6, column=3, columnspan=3, pady=10, sticky=W)
    label_sortable.grid(row=1, column=0, columnspan=3, pady=10, sticky=W)
    label_settings.grid(row=6, column=0, columnspan=3, pady=10, sticky=W)

    b_alike = Button(window, text="Merge Alike", width=15)
    b_alike.bind("<Button-1>", lambda e: it_lib.merge_alike_tracks())
    b_alike.grid(row=11, column=0, pady=10, sticky=W)
    
    b_alike = Button(window, text="Reset Library", width=15)
    b_alike.bind("<Button-1>", lambda e: it_lib.reset_tracks())
    b_alike.grid(row=11, column=1, pady=10)

    b_wtoggle = Button(window, text="Toggle Write", width=15)
    b_wtoggle.bind("<Button-1>", lambda e: it_lib.toggle_write_state())
    b_wtoggle.grid(row=7, column=0, pady=10, sticky=W)

    b_tpod = Button(window, text="Toggle Podcasts", width=15)
    b_tpod.bind("<Button-1>", lambda e: it_lib.toggle_podcasts())
    b_tpod.grid(row=7, column=1, pady=10)

    label3 = Label(window, text="Sorter:", font=("Times New Roman", 12))
    label3.grid(row=8, column=0, pady=10)
    
    selection = StringVar()
    types = ['Artist','Album','Track','Album artist', 'Genre', 'Rating', 'Year', 'Love']
    select = Combobox(textvariable=selection, values=types, width=12, state='readonly')
    select.current(0)
    select.grid(row=8, column=1, pady=10)
    
    file_choice = StringVar()
    files = find_libs()
    file_select = Combobox(textvariable=file_choice, values=files, width=45, state='readonly')
    file_select.current(0)
    file_select.grid(row=10, column=0, columnspan=3, pady=10, sticky=W)
    
    b_sub = Button(window, text="Subtract Backup Library:", width=33)
    b_sub.bind("<Button-1>", lambda e: it_lib.subtract_tracks(file_choice.get()))
    b_sub.grid(row=9, column=0, columnspan=2, pady=10, sticky=W)
    
    b_basics = Button(window, text="Basics", width=15)
    b_basics.bind("<Button-1>", lambda e: it_lib.print_basics())
    b_basics.grid(row=9, column=3, pady=10)
    
    b_times = Button(window, text="Total Time", width=15)
    b_times.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_times()])
    b_times.grid(row=2, column=1, pady=10)
    
    b_ratings = Button(window, text="Rating Info", width=15)
    b_ratings.bind("<Button-1>", lambda e: it_lib.print_rating_info(it_lib.rating_info()))
    b_ratings.grid(row=7, column=3, pady=10)
    
    b_plays = Button(window, text="Total Plays", width=15)
    b_plays.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_plays()])
    b_plays.grid(row=2, column=0, pady=10)
    
    b_ycount = Button(window, text="Year Counts", width=15)
    b_ycount.bind("<Button-1>", lambda e: it_lib.print_year_counts(it_lib.year_counts()))
    b_ycount.grid(row=8, column=3, pady=10)
    
    b_avrate = Button(window, text="Average Ratings", width=15)
    b_avrate.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_average_rating(it_lib.average_rating()[0], it_lib.average_rating()[1])])
    b_avrate.grid(row=3, column=2, pady=10)
    
    b_ppw = Button(window, text="Total PPW", width=15)
    b_ppw.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_plays_per_week()])
    b_ppw.grid(row=2, column=2, pady=10)
    
    b_avppw = Button(window, text="Average PPW", width=15)
    b_avppw.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_plays_per_week_average()])
    b_avppw.grid(row=2, column=3, pady=10)
    
    b_age = Button(window, text="Average Age", width=15)
    b_age.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_artist_average_years(it_lib.artist_average_year())])
    b_age.grid(row=3, column=3, pady=10)
    
    b_love = Button(window, text="Total Loves", width=15)
    b_love.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_loves()])
    b_love.grid(row=3, column=1, pady=10)
    
    b_lp = Button(window, text="Love Percentage", width=15)
    b_lp.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_love_percentage()])
    b_lp.grid(row=3, column=0, pady=10)
    
    b_at = Button(window, text="Average Length", width=15)
    b_at.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_average_times()])
    b_at.grid(row=4, column=0, pady=10)

    b_pu = Button(window, text="Percent Played", width=15)
    b_pu.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_percent_played()])
    b_pu.grid(row=4, column=1, pady=10)
    
    b_pu = Button(window, text="Last Plays", width=15)
    b_pu.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.print_average_last_plays()])
    b_pu.grid(row=4, column=2, pady=10)

    b_cd = Button(window, text="Create Lists Spreadsheet", width=45)
    b_cd.bind("<Button-1>", lambda e: [it_lib.set_sorter(selection.get()), it_lib.csv_dump()])
    b_cd.grid(row=5, column=0, pady=10, columnspan=4) 
    
    b_quit = Button(window, text="Backup", width=15)
    b_quit.bind("<Button-1>", lambda e: backup_library())
    b_quit.grid(row=11, column=3, pady=10)
        
    window.mainloop()
    
def convert_date(date):
    """Converts an iTunes date into seconds since Epoch"""
    date = date.split(sep='-')
    year = int(date[0])
    month = int(date[1])
    date = date[2].split(sep='T')
    day = int(date[0])
    time = date[1].split(sep=':')
    hours = int(time[0])
    minutes = int(time[1])
    time = (year, month, day, hours, minutes, 0, 0, 0, 0)
    return mktime(time)

def blank(line, strings):
    """Removes a list of strings from a large string"""
    for fragment in strings:
        line = line.replace(fragment, '')
    return line

class MakeDictionary(object):
    def __init__(self):
        """Resets track values"""
        self.plays = 0
        self.year = 0
        self.artist = '(no artist)'
        self.album_artist = '(no album artist)'
        self.time = 0
        self.title = '(no title)'
        self.rating = 0
        self.album = '(no album)'
        self.added = 0
        self.genre = '(no genre)'
        self.podcast = False
        self.loved = False

    def generate(self, file):
        """Creates a dictionary with song ids for keys"""
        tracks = {}
        for line in file:
            if '<key>Persistent ID</key>' in line:
                track_id = blank(line, ['\t\t\t<key>Persistent ID</key><string>', '</string>\n'])
            elif '<key>Podcast' in line:
                self.podcast = True
            elif '<key>Year</key><integer>' in line:
                self.year = blank(line, ['<key>Year</key><integer>', '</integer>'])
            elif '<key>Play Count</key><integer>' in line:
                self.plays = blank(line, ['<key>Play Count</key><integer>', '</integer>'])
            elif '<key>Name</key><string>' in line:
                self.title = blank(line, ['\t\t\t<key>Name</key><string>', '</string>\n'])
            elif '<key>Artist</key><string>' in line:
                self.artist = blank(line, ['\t\t\t<key>Artist</key><string>', '</string>\n'])
            elif '<key>Album</key><string>' in line:
                self.album = blank(line, ['\t\t\t<key>Album</key><string>', '</string>\n'])
            elif '<key>Album Artist</key><string>' in line:
                self.album_artist = blank(line, ['\t\t\t<key>Album Artist</key><string>', '</string>\n'])
            elif '<key>Total Time</key><integer>' in line:
                self.time = blank(line, ['<key>Total Time</key><integer>', '</integer>'])
            elif '<key>Rating</key><integer>' in line:
                self.rating = blank(line, ['<key>Rating</key><integer>', '</integer>'])
            elif '<key>Date Added</key><date>' in line:
                self.added = blank(line, ['<key>Date Added</key><date>', '</date>'])
            elif '<key>Genre</key><string>' in line:
                self.genre = blank(line, ['\t\t\t<key>Genre</key><string>', '</string>\n'])
            elif '<key>Loved</key><true/>' in line:
                self.loved = True
            elif '<key>Play Date</key>' in line:
                self.last_played = blank(line, ['<key>Play Date</key><integer>', '</integer>'])
            elif '<key>Location' in line:
                tracks[track_id] = Track(self.title,
                                         self.plays,
                                         self.time,
                                         self.year,
                                         self.artist,
                                         self.rating,
                                         self.album_artist,
                                         self.album,
                                         convert_date(self.added),
                                         self.genre,
                                         self.loved,
                                         self.podcast,
                                         self.last_played)
                self.__init__()
            elif '<key>Playlists</key>' in line:
                break
        return tracks

def main():
    """Main function"""
    it_lib = Library(load_file())
    gui_window(it_lib)

if __name__ == "__main__":
    main()