import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Query12Component } from './query12.component';

describe('Query12Component', () => {
  let component: Query12Component;
  let fixture: ComponentFixture<Query12Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Query12Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Query12Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
