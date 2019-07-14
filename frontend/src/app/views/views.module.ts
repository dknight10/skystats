import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

import { ViewsRoutingModule } from './views-routing.module';
import { SessionsComponent } from './sessions/sessions.component';


@NgModule({
  declarations: [SessionsComponent],
  imports: [
    CommonModule,
    ViewsRoutingModule,
    HttpClientModule
  ]
})
export class ViewsModule { }
