import pytest
import psutil
from incl import SystemMonitor  # Замените на фактический путь к вашему модулю


@pytest.fixture
def system_monitor():
    return SystemMonitor()


def test_get_memory_usage(system_monitor):
    memory_usage = system_monitor.get_memory_usage()
    assert isinstance(memory_usage, float)
    assert memory_usage == psutil.virtual_memory()[2]


def test_get_swap_usage(system_monitor):
    swap_usage = system_monitor.get_swap_usage()
    assert isinstance(swap_usage, float)
    assert swap_usage == psutil.swap_memory()[3]


def test_get_cpu_usage(system_monitor):
    cpu_usage = system_monitor.get_cpu_usage()
    assert isinstance(cpu_usage, float)
    assert cpu_usage == psutil.cpu_percent()


def test_get_disk_usage(system_monitor):
    disk_usage = system_monitor.get_disk_usage()
    assert isinstance(disk_usage, list)
    for partition, usage in disk_usage:
        assert isinstance(partition, str)
        assert isinstance(usage, float)
        assert 0 <= usage <= 100
