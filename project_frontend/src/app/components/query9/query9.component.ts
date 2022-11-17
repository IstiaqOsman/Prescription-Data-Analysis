import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query9',
  templateUrl: './query9.component.html',
  styleUrls: ['./query9.component.css']
})
export class Query9Component implements OnInit {
  data_all: any[] = [];
  items: any[] = [];
  division: any[] = [];
  sales: any[] = [];

  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit(): void {
    this.Query9Data();
  }

  Query9Data(): void{
    this.queryService.getQuery9().subscribe((data:any)=>{
        console.log(data);
        for(const d of data){
          //console.log(d.Sales, d.Type)
          this.items.push(d.Item)
          this.division.push(d.Division)
          this.sales.push(d.Sales)
        }
        this.data_all = data;
      }
    )
  }

}
