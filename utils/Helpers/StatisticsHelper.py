import os
from multiprocessing import Process

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from Data.Utilities import open_csv
from utils import routes
from utils.Helpers.AnalystHelper import *

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


def graph_1(analysts_ID, analysts_daily_avg):  # Daily ability
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.bar(analysts_ID, analysts_daily_avg)
    ax.set_xlabel('Analyst ID')
    ax.set_ylabel('Daily avg')
    ax.set_title('Daily ability')
    # plt.show()


def graph_2(analysts_ID, duration_mean):  # issues duration-mean (in-prog -> done) Comparison
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.plot(analysts_ID, duration_mean)
    ax.set_xlabel('Analyst ID')
    ax.set_ylabel('Duration mean [h]')
    ax.set_title('Duration-mean comparison ')
    # plt.show()


def graph_3(analyst_ID, issues_duration, issues_impact):  # impact against time to complete per analyst
    fig, ax = plt.subplots()
    ax.scatter(issues_duration, issues_impact, s=50, facecolor='C0', edgecolor='k')
    ax.set_xlabel('Duration')
    ax.set_ylabel('Impact')
    ax.set_title("{} - impact VS duration.".format(analyst_ID.capitalize()))
    # plt.show()


# graph_1(['analyst_1', 'analyst_2', 'analyst_3', 'analyst_4'], [3, 1, 5, 7])
# graph_2(['analyst_1', 'analyst_2', 'analyst_3', 'analyst_4'], [2.5, 1, 3.5, 3])
# graph_3('analyst_1', [3, 2, 1.5, 5, 3.2, 4], [20, 45, 15, 50, 30, 40])

def get_graphs_pdf():
    df = open_csv(routes.status_table)
    path = f'{routes.statsDir}/analystStat.pdf'
    analyst_list = list(set(df['Analyst Handler']))
    daily_avg_list = []
    done_avg_list = []

    for analyst in analyst_list:
        analyst_daily_avg = daily_avg_issues(df, analyst)
        daily_avg_list.append(analyst_daily_avg['ave_per_day'])

        analyst_done_avg = done_issue_avg(df, analyst)
        done_avg_list.append(round(analyst_done_avg['duration_mean']))

    analyst_list.append('itay')  # for example
    daily_avg_list.append(4)  # for example
    done_avg_list.append(15)  # for example

    if os.path.exists(path):
        os.remove(path)

    pdf = PdfPages(path)

    graph_2(analyst_list, done_avg_list)
    pdf.savefig()
    graph_1(analyst_list, daily_avg_list)
    pdf.savefig()

    for analyst in analyst_list:
        influence_dict = duration_and_impact(df, analyst)
        if not influence_dict:
            print('{} got empty dataFrame, graph3 not created'.format(analyst))
            continue
        duration = [x[0] for x in influence_dict.values()]
        influence = [x[1] for x in influence_dict.values()]
        graph_3(analyst, duration, influence)
        pdf.savefig()
    pdf.close()

# get_graphs_pdf()
