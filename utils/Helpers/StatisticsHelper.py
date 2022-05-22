import os
import sys
from multiprocessing import Process

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import Data.Utilities as Data
from Data.Utilities import open_csv, get_now
from utils import routes
from utils.Helpers.AnalystHelper import *
from utils.Helpers.GeneralHelpers import *

__all__ = ["call_stat_graph", "graph_1", "graph_2", "graph_3", "get_graphs_pdf"]


# This function generates the graph using multiproccess
def call_stat_graph(graphX, *_args):
    p = Process(target=graphX, args=_args)
    try:
        p.start()
    except:
        print("Couldn't start the process.")
    finally:
        return


def first_page():
    firstPage = plt.figure(figsize=(5, 2.7))
    firstPage.clf()
    txt = 'Statistic PDF\n'
    date = get_now() + '\n'
    firstPage.text(0.5, 0.5, txt + date, transform=firstPage.transFigure, size=24, ha="center")


def graph_1(analysts_ID, analysts_daily_avg):  # Daily ability
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.bar(analysts_ID, analysts_daily_avg)
    ax.set_xlabel('Analyst ID')
    ax.set_ylabel('Daily avg')
    ax.set_title('Daily ability')
    # plt.show()


def graph_2(analysts_ID, duration_mean):  # issues duration-mean (in-prog -> done) Comparison
    fig, ax = plt.subplots(figsize=(5, 3.7))
    ax.plot(analysts_ID, duration_mean)
    ax.set_xlabel('Analyst ID')
    ax.set_ylabel('Duration mean [h]')
    ax.set_title('Duration-mean comparison ')

    # plt.show()


def graph_3(analyst_ID, issues_duration, issues_impact):  # impact against time to complete per analyst
    fig, ax = plt.subplots(figsize=(5, 3.7))
    ax.scatter(issues_duration, issues_impact, s=50, facecolor='C0', edgecolor='k')
    ax.set_xlabel('Duration')
    ax.set_ylabel('Impact')
    ax.set_title("{} - impact VS duration.".format(analyst_ID.capitalize()))
    # plt.show()


def graph_4(analyst_ID, analysts_daily_avg, issues_impact_dict):
    f = plt.figure(figsize=(5, 3.7))
    ax = f.add_subplot(111)
    duration = 4  # days forward
    x_labels = [str(x + 1) for x in range(duration)]
    len_of_values = [len(l) for l in list(issues_impact_dict.values())]
    print(issues_impact_dict, '->', len_of_values, '->', analysts_daily_avg)
    counter = [sum(len_of_values[i:i + analysts_daily_avg]) for i in range(0, len(len_of_values), analysts_daily_avg)][
              :duration]
    counter.extend([0 for _ in range(0, duration - len(counter))])
    bars = plt.bar(x_labels, counter)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., 1.0 * height,
                 '%0.2f' % height, va='bottom', ha='center')

    plt.text(0.8, 0.95, 'based on {} issues per day'.format(analysts_daily_avg), ha='center', va='center',
             transform=ax.transAxes)

    plt.ylim(0, max(counter) + 2)
    plt.title("{} - Most effective, 4 days plan".format(analyst_ID.capitalize()))


# graph_1(['analyst_1', 'analyst_2', 'analyst_3', 'analyst_4'], [3, 1, 5, 7])
# graph_2(['analyst_1', 'analyst_2', 'analyst_3', 'analyst_4'], [2.5, 1, 3.5, 3])
# graph_3('analyst_1', [3, 2, 1.5, 5, 3.2, 4], [20, 45, 15, 50, 30, 40])
# graph_4('yaniv', 2, {'a': [1, 2, 3], 'b': [1, 2, 3, 1, 2, 3, 1, 2, 3], 'v': [1, 2, 3], 's': [1, 2, 3, 4, 5, 6]})

def get_graphs_pdf():
    status_df = open_csv(routes.status_table)
    raw_df = Data.raw_dataFrame

    path = f'{routes.statsDir}/analystStat.pdf'
    analyst_list = list(set(status_df['Analyst Handler']))
    daily_avg_list = []
    done_avg_list = []

    for analyst in analyst_list:
        analyst_daily_avg = daily_avg_issues(status_df, analyst)
        daily_avg_list.append(analyst_daily_avg['ave_per_day'])

        analyst_done_avg = done_issue_avg(status_df, analyst)
        done_avg_list.append(round(analyst_done_avg['duration_mean']))

    # ---- example-----
    analyst_list.append('itay')
    daily_avg_list.append(4)
    done_avg_list.append(15)

    analyst_list.append('ben')
    daily_avg_list.append(6)
    done_avg_list.append(20)
    # ---- example-----

    if os.path.exists(path):
        os.remove(path)

    pdf = PdfPages(path)
    try:
        first_page()
        pdf.savefig()
        graph_2(analyst_list, done_avg_list)
        pdf.savefig()
        graph_1(analyst_list, daily_avg_list)
        pdf.savefig()

        # ---- example-----
        # graph_3('itay', [3, 12, 1.5, 15, 8, 12], [20, 45, 15, 50, 30, 40])
        # pdf.savefig()
        # ---- example-----

        for analyst in analyst_list:
            influence_dict = duration_and_impact(status_df, analyst)
            if not influence_dict:
                print('{} got empty dataFrame, graph3 not created'.format(analyst))
                continue
            duration = [x[0] for x in influence_dict.values()]
            influence = [x[1] for x in influence_dict.values()]
            graph_3(analyst, duration, influence)
            pdf.savefig()

            analyst_df = hide_handled_issues(raw_df, status_df, analyst)
            influence_dict = find_most_influential(analyst_df, raw_df)
            influence_dict = sort_dict_by_values(influence_dict)
            daily_avg = daily_avg_issues(status_df, analyst)
            daily_avg = int(daily_avg['ave_per_day'])
            graph_4(analyst, daily_avg, influence_dict)
            pdf.savefig()
    except Exception as e:
        print(e)

    pdf.close()

# get_graphs_pdf()
