import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

import { MatTableModule } from '@angular/material/table';

import { ViewsRoutingModule } from './views-routing.module';
import { SessionsComponent } from './sessions/sessions.component';


@NgModule({
  declarations: [SessionsComponent],
  imports: [
    CommonModule,
    ViewsRoutingModule,
    HttpClientModule,
    MatTableModule
  ]
})
export class ViewsModule { }
