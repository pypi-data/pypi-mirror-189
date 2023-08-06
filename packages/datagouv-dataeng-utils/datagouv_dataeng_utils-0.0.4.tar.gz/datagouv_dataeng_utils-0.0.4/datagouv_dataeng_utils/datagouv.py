from typing import Union, List, Optional, TypedDict
import requests
import os

DATAGOUV_URL = {"prod": "https://www.data.gouv.fr", "demo": "https://demo.data.gouv.fr"}


class File(TypedDict):
    dest_name: str
    dest_path: str


def create_dataset(
    api_key: str,
    payload: TypedDict,
    env: Optional[str] = "prod",
):
    """Create a dataset in data.gouv.fr

    Args:
        api_key (str): API key from data.gouv.fr
        payload (TypedDict): payload for dataset containing at minimum title
        env (Optional[str], optional): data.gouv.fr env (prod or demo). Defaults to "prod".

    Returns:
        json: return API result in a dictionnary
    """
    headers = {
        "X-API-KEY": api_key,
    }
    r = requests.post(
        "{}/api/1/datasets/".format(DATAGOUV_URL[env]), json=payload, headers=headers
    )
    return r.json()


def get_resource(
    resource_id: str,
    file_to_store: File,
    env: Optional[str] = "prod",
):
    """Download a resource in data.gouv.fr

    Args:
        resource_id (str): ID of the resource
        file_to_store (File): Dictionnary containing `dest_path` and
        `dest_name` where to store downloaded resource
        env (Optional[str], optional): data.gouv.fr env (prod or demo). Defaults to "prod".

    """
    with requests.get(
        f"{DATAGOUV_URL[env]}/fr/datasets/r/{resource_id}", stream=True
    ) as r:
        r.raise_for_status()
        os.makedirs(os.path.dirname(file_to_store["dest_path"]), exist_ok=True)
        with open(
            f"{file_to_store['dest_path']}{file_to_store['dest_name']}", "wb"
        ) as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


def post_resource(
    api_key: str,
    file_to_upload: File,
    dataset_id: str,
    resource_id: Optional[str] = None,
    env: Optional[str] = "prod",
):
    """Upload a resource in data.gouv.fr

    Args:
        api_key (str): API key from data.gouv.fr
        file_to_upload (File): Dictionnary containing `dest_path` and
        `dest_name` where resource to upload is stored
        dataset_id (str): ID of the dataset where to store resource
        resource_id (Optional[str], optional): ID of the resource where
        to upload file. If it is a new resource, let it to None.
        Defaults to None.
        env (Optional[str], optional): data.gouv.fr env (prod or demo). Defaults to "prod".

    Returns:
        json: return API result in a dictionnary
    """
    headers = {
        "X-API-KEY": api_key,
    }
    files = {
        "file": open(
            "{}{}".format(file_to_upload["dest_path"], file_to_upload["dest_name"]),
            "rb",
        )
    }
    if resource_id:
        url = "{}/api/1/datasets/{}/resources/{}/upload/".format(
            DATAGOUV_URL[env],
            dataset_id,
            resource_id,
        )
    else:
        url = "{}/api/1/datasets/{}/upload/".format(
            DATAGOUV_URL[env],
            dataset_id,
        )
    r = requests.post(url, files=files, headers=headers)
    return r.json()


def delete_dataset_or_resource(
    api_key: str,
    dataset_id: str,
    resource_id: Optional[str] = None,
    env: Optional[str] = "prod",
):
    """Delete a dataset or a resource in data.gouv.fr

    Args:
        api_key (str): API key from data.gouv.fr
        dataset_id (str): ID of the dataset
        resource_id (Optional[str], optional): ID of the resource.
        If resource is None, the dataset will be deleted. Else only the resource.
        Defaults to None.
        env (Optional[str], optional): data.gouv.fr env (prod or demo). Defaults to "prod".

    Returns:
        json: return API result in a dictionnary
    """
    headers = {
        "X-API-KEY": api_key,
    }
    if resource_id:
        url = "{}/api/1/datasets/{}/resources/{}/".format(
            DATAGOUV_URL[env],
            dataset_id,
            resource_id,
        )
    else:
        url = "{}/api/1/datasets/{}/".format(
            DATAGOUV_URL[env],
            dataset_id,
        )

    r = requests.delete(url, headers=headers)
    if r.status_code == 204:
        return {"message": "ok"}
    else:
        return r.json()


def get_dataset_or_resource_metadata(
    dataset_id: str,
    resource_id: Optional[str] = None,
    env: Optional[str] = "prod",
):
    """Retrieve dataset or resource metadata from data.gouv.fr

    Args:
        dataset_id (str): ID ot the dataset
        resource_id (Optional[str], optional): ID of the resource.
        If resource_id is None, it will be dataset metadata which will be
        returned. Else it will be resouce_id's ones. Defaults to None.
        env (Optional[str], optional): data.gouv.fr env (prod or demo). Defaults to "prod".

    Returns:
       json: return API result in a dictionnary containing metadatas
    """
    if resource_id:
        url = "{}/api/1/datasets/{}/resources/{}/".format(
            DATAGOUV_URL[env], dataset_id, resource_id
        )
    else:
        url = "{}/api/1/datasets/{}".format(
            DATAGOUV_URL[env],
            dataset_id,
        )
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return {"message": "error", "status": r.status_code}


def get_dataset_from_resource_id(
    resource_id: str,
    env: Optional[str] = "prod",
):
    """Return dataset ID from resource ID from data.gouv.fr

    Args:
        resource_id (str): ID of a resource
        env (Optional[str], optional): data.gouv.fr env (prod or demo). Defaults to "prod".

    Returns:
       json: return API result in a dictionnary containing metadatas
    """
    url = "{}/api/2/datasets/resources/{}/".format(
        DATAGOUV_URL[env], resource_id
    )
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()

def update_dataset_or_resource_metadata(
    api_key: str,
    payload: TypedDict,
    dataset_id: str,
    resource_id: Optional[str] = None,
    env: Optional[str] = "prod",
):
    """Update metadata to dataset or resource in data.gouv.fr

    Args:
        api_key (str): API key from data.gouv.fr
        payload (TypedDict): metadata to upload.
        dataset_id (str): ID of the dataset
        resource_id (Optional[str], optional): ID of the resource.
        If resource_id is None, it will be dataset metadata which will be
        updated. Else it will be resouce_id's ones. Defaults to None.
        env (Optional[str], optional): data.gouv.fr env (prod or demo). Defaults to "prod".

    Returns:
       json: return API result in a dictionnary containing metadatas
    """
    headers = {
        "X-API-KEY": api_key,
    }
    if resource_id:
        url = "{}/api/1/datasets/{}/resources/{}/".format(
            DATAGOUV_URL[env],
            dataset_id,
            resource_id,
        )
    else:
        url = "{}/api/1/datasets/{}/".format(
            DATAGOUV_URL[env],
            dataset_id,
        )

    r = requests.put(url, json=payload, headers=headers)
    return r.json()


def update_dataset_or_resource_extras(
    api_key: str,
    payload: TypedDict,
    dataset_id: str,
    resource_id: Optional[str] = None,
    env: Optional[str] = "prod",
):
    """Update specific extras to a dataset or resource in data.gouv.fr

    Args:
        api_key (str): API key from data.gouv.fr
        payload (TypedDict): Payload contaning extra and its value
        dataset_id (str): ID of the dataset.
        resource_id (Optional[str], optional): ID of the resource.
        If resource_id is None, it will be dataset extras which will be
        updated. Else it will be resouce_id's ones. Defaults to None.
        env (Optional[str], optional): data.gouv.fr env (prod or demo). Defaults to "prod".

    Returns:
       json: return API result in a dictionnary containing metadatas
    """
    headers = {
        "X-API-KEY": api_key,
    }
    if resource_id:
        url = "{}/api/2/datasets/{}/resources/{}/extras/".format(
            DATAGOUV_URL[env],
            dataset_id,
            resource_id,
        )
    else:
        url = "{}/api/2/datasets/{}/extras/".format(
            DATAGOUV_URL[env],
            dataset_id,
        )

    r = requests.put(url, json=payload, headers=headers)
    return r.json()


def delete_dataset_or_resource_extras(
    api_key: str,
    extras: List,
    dataset_id: str,
    resource_id: Optional[str] = None,
    env: Optional[str] = "prod",
):
    """Delete extras from a dataset or resoruce in data.gouv.fr

    Args:
        api_key (str): API key from data.gouv.fr
        extras (List): List of extras to delete.
        dataset_id (str): ID of the dataset.
        resource_id (Optional[str], optional): ID of the resource.
        If resource_id is None, it will be dataset extras which will be
        deleted. Else it will be resouce_id's ones. Defaults to None.
        env (Optional[str], optional): data.gouv.fr env (prod or demo). Defaults to "prod".

    Returns:
       json: return API result in a dictionnary containing metadatas
    """
    headers = {
        "X-API-KEY": api_key,
    }
    if resource_id:
        url = "{}/api/2/datasets/{}/resources/{}/extras/".format(
            DATAGOUV_URL[env],
            dataset_id,
            resource_id,
        )
    else:
        url = "{}/api/2/datasets/{}/extras/".format(
            DATAGOUV_URL[env],
            dataset_id,
        )

    r = requests.delete(url, json=extras, headers=headers)
    if r.status_code == 204:
        return {"message": "ok"}
    else:
        return r.json()
