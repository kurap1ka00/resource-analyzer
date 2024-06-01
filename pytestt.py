import pytest

from incl import SystemMonitor  # Замените на фактический путь к вашему модулю
import os
import json

@pytest.fixture
def system_state():
    return {"gpu_memory_usage": 16, "memory_usage": 47, "swap_usage": 4, "cpu_usage": 14, "disk_usage": []}


@pytest.fixture
def system_monitor():
    return SystemMonitor()


def test_load_state(system_monitor):
    ss=system_state()
    
    ss1=system_monitor.load_state()
    
    assert ss["gpu_memory_usage"]==ss1["gpu_memory_usage"]

def test_get_memory_usage(system_monitor):
    memory_usage = system_monitor.get_memory_usage()
    assert isinstance(memory_usage, float)
    assert 0 <= memory_usage <= 100


def test_get_swap_usage(system_monitor):
    swap_usage = system_monitor.get_swap_usage()
    assert isinstance(swap_usage, float)
    assert 0 <= swap_usage<= 100


def test_get_cpu_usage(system_monitor):
    cpu_usage = system_monitor.get_cpu_usage()
    assert isinstance(cpu_usage, float)
    assert 0 <= cpu_usage <= 100


def test_get_disk_usage(system_monitor):
    disk_usage = system_monitor.get_disk_usage()
    assert isinstance(disk_usage, list)
    for partition, usage in disk_usage:
        assert isinstance(partition, str)
        assert isinstance(usage, float)
        assert 0 <= usage <= 100
