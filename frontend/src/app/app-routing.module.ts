import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Query1Component } from './components/query1/query1.component';
import { Query2Component } from './query2/query2.component';

const routes: Routes = [
  {path: 'query1', component: Query1Component},
  {path: 'query2', component: Query2Component},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
