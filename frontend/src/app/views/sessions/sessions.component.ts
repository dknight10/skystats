import { Component, OnInit } from '@angular/core';

import { SelectionModel } from '@angular/cdk/collections';
import { MatTableDataSource } from '@angular/material/table';

import { SessionsService } from './sessions.service';
import { Session } from './session';

@Component({
  selector: 'skystats-sessions',
  templateUrl: './sessions.component.html',
  styleUrls: ['./sessions.component.scss']
})
export class SessionsComponent implements OnInit {
  dataSource = new MatTableDataSource<Session>();
  selection = new SelectionModel<Session>(true, []);
  displayedColumns = ["select", "timestamp", "name", "type", "shots", "clubs"];

  constructor(private service: SessionsService) { }

  isAllSelected() {
    const numSelected = this.selection.selected.length;
    const numRows = this.dataSource.data.length;
    return numSelected === numRows;
  }

  masterToggle() {
    this.isAllSelected() ?
      this.selection.clear() :
      this.dataSource.data.forEach(row => this.selection.select(row));
  }

  ngOnInit() {
    this.service.getSessions().subscribe(data => {
      this.dataSource.data = data
      this.masterToggle();  // select all rows initially
    });
  }

  noneSelected() {
    return this.selection.selected.length === 0;
  }

  download() {
    if (this.noneSelected()) {
      return;
    }
    let ids = this.selection.selected.map(row => row.id);
    let format = 'excel';
    this.service.download(ids, format);
  }
}
