import {Component, OnInit} from '@angular/core';
import {Chart} from 'node_modules/chart.js';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query12',
  templateUrl: './query12.component.html',
  styleUrls: ['./query12.component.css']
})

export class Query12Component implements OnInit {

  data_all: any[] = [];
  sales: any[] = [];
  chapter: any[] = [];
  count: any[] = [];
  month: any[] = [];

  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit(): void {
    this.queryService.getQuery8().subscribe((data: any) => {
        console.log(data)
        for (const d of data) {
          this.chapter.push(d.BNF_CHAPTER)
          this.sales.push(d.Sales)
          this.count.push(d.Count)
          this.month.push(d.MONTH)
        }
        this.data_all = data;
      }
    )
    let delayed: boolean;

    const myChart = new Chart("myChart", {

      type: 'bar',

      data: {

        labels: this.chapter,

        datasets: [{
          label: 'Sales',
          data: this.sales,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1
        }, {
          type: 'line',
          label: 'Visit Count',
          data: this.count,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1

        }
        ]
      },
      options: {

/*      animation: {

        onComplete: () => {
          delayed = true;
        },
        delay: (context) => {
          let delay = 0;
          if (context.type === 'data' && context.mode === 'default' && !delayed) {
            delay = context.dataIndex * 10000 + context.datasetIndex * 200;
          }
          return delay;
        }
      }*/
      },

    });
  }

}
