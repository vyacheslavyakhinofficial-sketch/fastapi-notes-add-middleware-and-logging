from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_task_service
from app.schemas.file import TaskCreate, TaskRead, TaskUpdate
from app.services.file import TaskNotFoundError, TaskService

from app.api.dependencies import get_category_service
from app.schemas.file import CategoryCreate, CategoryRead, CategoryUpdate
from app.services.file import CategoryNotFoundError, CategoryService


task_router = APIRouter(prefix="/tasks", tags=["tasks"])


@task_router.get("", response_model=list[TaskRead])
def get_tasks(service: TaskService = Depends(get_task_service)) -> list[TaskRead]:
    return service.list_tasks()


@task_router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    service: TaskService = Depends(get_task_service),
) -> TaskRead:
    return service.create_task(payload)


@task_router.patch("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: str,
    payload: TaskUpdate,
    service: TaskService = Depends(get_task_service),
) -> TaskRead:
    try:
        return service.update_task(task_id, payload)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена",
        )


@task_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: str,
    service: TaskService = Depends(get_task_service),
) -> None:
    try:
        service.delete_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена",
        )




category_router = APIRouter(prefix="/categories", tags=["categories"])


@category_router.get("", response_model=list[CategoryRead])
def get_categories(service: CategoryService = Depends(get_category_service)) -> list[CategoryRead]:
    return service.list_categories()


@category_router.post("", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category(
    payload: CategoryCreate,
    service: CategoryService = Depends(get_category_service),
) -> CategoryRead:
    return service.create_category(payload)


@category_router.patch("/{category_id}", response_model=CategoryRead)
def update_category(
    category_id: str,
    payload: CategoryUpdate,
    service: CategoryService = Depends(get_category_service),
) -> CategoryRead:
    try:
        return service.update_category(category_id, payload)
    except CategoryNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Категория не найдена",
        )


@category_router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: str,
    service: CategoryService = Depends(get_category_service),
) -> None:
    try:
        service.delete_category(category_id)
    except CategoryNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Категория не найдена",
        )