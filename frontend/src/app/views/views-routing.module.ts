import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SessionsComponent } from './sessions/sessions.component';

const routes: Routes = [
    { path: '', component: SessionsComponent },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ViewsRoutingModule { }