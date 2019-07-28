import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthGuard } from '../auth/auth.guard';

import { SessionsComponent } from './sessions/sessions.component';

const routes: Routes = [
    {
        path: '', canActivate: [AuthGuard], children: [
            { path: '', component: SessionsComponent },
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ViewsRoutingModule { }