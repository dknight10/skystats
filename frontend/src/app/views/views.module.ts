import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

import { MatTableModule } from '@angular/material/table';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

import { ViewsRoutingModule } from './views-routing.module';
import { SessionsComponent } from './sessions/sessions.component';


@NgModule({
  declarations: [SessionsComponent],
  imports: [
    CommonModule,
    ViewsRoutingModule,
    HttpClientModule,
    MatTableModule,
    MatCheckboxModule,
    MatButtonModule,
    MatIconModule
  ]
})
export class ViewsModule { }
