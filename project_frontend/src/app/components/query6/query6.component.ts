import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";
import {Chart} from "chart.js";

@Component({
  selector: 'app-query6',
  templateUrl: './query6.component.html',
  styleUrls: ['./query6.component.css']
})

export class Query6Component implements OnInit {
  data_all: any[] = [];
  month: any[] = [];
  chapter: any[] = [];
  count: any[] = [];




  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query6Data();
  }
  query6Data(): void {
    this.queryService.getQuery6().subscribe((data: any) => {
        console.log(data);
        for (const d of data) {
          this.month.push(d.MONTH)
          this.chapter.push(d.BNF_CHAPTER)
          this.count.push(d.COUNT)
        }
      this.data_all = data;
      }
    )
    const myChart = new Chart("myChart", {
      type: 'bar',

      data: {

        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],

        datasets: [{
          label: 'Cardiovascular System',
          data: [1532, 1532, 1423, 1479, 1603, 1520, 1463, 1510, 1452, 1535, 1365, 1464],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
/*            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'*/
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
/*            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'*/
          ],
          borderWidth: 1
        }, {
          label: 'Central Nervous System',
          data: [2601, 2560, 2616, 2500, 2554, 2507, 2598, 2590, 2561, 2565, 2660, 2550],
          backgroundColor: [
/*            'rgba(255, 99, 132, 0.2)',*/
            'rgba(54, 162, 235, 0.2)',
/*            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'*/
          ],
          borderColor: [
/*            'rgba(255, 99, 132, 1)',*/
            'rgba(54, 162, 235, 1)',
/*            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'*/
          ],
          borderWidth: 1

        }, {
          label: 'Endocrine System',
          data: [954, 930, 906, 946, 929, 937, 899, 924, 891, 933, 915, 953],
          backgroundColor: [
/*            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',*/
            'rgba(255, 206, 86, 0.2)',
/*            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'*/
          ],
          borderColor: [
/*            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',*/
            'rgba(255, 206, 86, 1)',
            // 'rgba(75, 192, 192, 1)',
            // 'rgba(153, 102, 255, 1)',
            // 'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1

        }
        ]
      },
      options: {
        scales: {
          x: {
            stacked: true
          },
          y: {
            stacked: true
          }
        }
      }
    });
  }

}
